with open(r'data/VOCdevkit/2007_test.txt', 'r', encoding='utf-8') as fr:
    images = fr.readlines()
    for i, image in enumerate(images):
        with open(image.strip(), 'rb') as f:
            image_content = f.read()
            fw = open(f'data/samples/test{i+1}.jpg', 'wb')
            fw.write(image_content)
            fw.close()
