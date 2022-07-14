import os
import cv2

list_of_names = []


def delete_old_data():
   for i in os.listdir("generated-certificated-data/"):
      os.remove("generated-certificated-data/{}".format(i))

def cleanup_the_data():
    with open ("names.txt") as file:
        for line in file:
            list_of_names.append(line.strip())

def generate_certificates():
    for index, name in enumerate(list_of_names):
        template = cv2.imread("globalcoderzclasscertificate.jpg")
        cv2.putText(template, name, (569, 2447), cv2.FONT_HERSHEY_COMPLEX_SMALL, 15, (0, 0, 0), 15, cv2.LINE_AA)
        cv2.imwrite(f'generated-certificated-data/{name}.jpg', template)
        print("Generating {} / {}".format(index + 1,len(list_of_names)))

def main():
   delete_old_data()
   cleanup_the_data()
   generate_certificates()

if __name__ == '__main__':
   main()