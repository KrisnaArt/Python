# importing libraries
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torchvision import datasets
from torch.utils.data import DataLoader
from PIL import Image

def learn_user_face():
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    mtcnn = MTCNN(image_size=240, margin=0, min_face_size=20, device=device)  # initializing mtcnn for face detection
    resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)  # initializing resnet for face img to embeding conversion

    dataset = datasets.ImageFolder('fotoWajah/learn')  # photos folder path
    idx_to_class = {i: c for c, i in dataset.class_to_idx.items()}  # accessing names of peoples from folder names

    def collate_fn(x):
        return x[0]

    loader = DataLoader(dataset, collate_fn=collate_fn)

    face_list = []  # list of cropped faces from photos folder
    name_list = []  # list of names corrospoing to cropped photos
    embedding_list = []  # list of embeding matrix after conversion from cropped faces to embedding matrix using resnet

    for img, idx in loader:
        face, prob = mtcnn(img, return_prob=True)

        if face is not None and prob > 0.90:  # if face detected and porbability > 90%
            if torch.cuda.is_available():
                face = face.cuda()

            emb = resnet(face.unsqueeze(0))  # passing cropped face into resnet model to get embedding matrix

            embedding_list.append(emb.detach())  # resulten embedding matrix is stored in a list
            name_list.append(idx_to_class[idx])  # names are stored in a list

    data = [embedding_list, name_list]
    torch.save(data, 'data.pt')  # saving data.pt file

    print ("----recog")

    return "oke"

def detect_user_face(file_path):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    mtcnn = MTCNN(image_size=240, margin=0, min_face_size=20, device=device)  # initializing mtcnn for face detection
    resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)  # initializing resnet for face img to embeding conversion

    model = torch.load('data.pt')

    def face_match():  # img_path= location of photo, data_path= location of data.pt
        # getting embedding matrix of the given img
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.open(file_path)
        #img = Image.fromarray(img)
        face, prob = mtcnn(img, return_prob=True)  # returns cropped face and probability

        name_list = model[1]  # getting list of names
        dist_list = []  # list of matched distances, minimum distance is used to identify the person

        if face is not None:
            if torch.cuda.is_available():
                face = face.cuda()

            emb = resnet(face.unsqueeze(0)).detach()  # detech is to make required gradient false

            # saved_data = torch.load('data.pt')  # loading data.pt file
            embedding_list = model[0]  # getting embedding data

            for idx, emb_db in enumerate(embedding_list):
                dist = torch.dist(emb, emb_db).item()
                dist_list.append(dist)

            idx_min = dist_list.index(min(dist_list))

            return (name_list[idx_min], min(dist_list))
        else:
            return None
    result = face_match()
    print('Face matched with: ', result[0], 'With distance: ', result[1])

    return result[0]