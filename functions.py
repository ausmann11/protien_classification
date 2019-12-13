###
# THIS FILE CONTAINS BASE FUNCTIONS REFERENCED IN OTHER FILES
###


###
# Breaks an large image up into smaller sections with one main protein per box
###
def extract_detections(image, blobs, min_offset=5, scaling=1):
    detection_list = []
    # iterate through all the detections
    for blob in blobs:

        # turn the float values to integers
        x, y, offset = np.trunc(blob).astype(np.int)

        # set the size of the box to be formed
        scaled_offset = offset * scaling

        # set the corners
        xmin = x - scaled_offset
        xmax = x + scaled_offset
        ymin = y - scaled_offset
        ymax = y + scaled_offset

        # weed out too small of a detection
        if offset <= min_offset:
            pass

        # check coordinates after offset are within the bounds of
        #      the image
        elif (xmin >= 0 and ymin >= 0) and (
            xmax < image.shape[0] and ymax < image.shape[1]
        ):
            # create slice out a box around the detection
            # print("Image found at {},{}".format(x,y))
            img_slice = image[xmin:xmax, ymin:ymax]
            # add it to the list
            detection_list.append(img_slice)

        # an object is found at the edge
        elif xmin < 0:
            if ymin < 0:
                # print("Image found at {},{}".format(x,y))
                img_slice = image[0:xmax, 0:ymax]
                detection_list.append(img_slice)
            else:
                # print("Image found at {},{}".format(x,y))
                img_slice = image[0:xmax, ymin:ymax]
                detection_list.append(img_slice)
        elif xmax >= image.shape[0]:
            # print("Image found at {},{}".format(x,y))
            if ymax >= image.shape[1]:
                img_slice = image[xmin:-1, ymin:-1]
                detection_list.append(img_slice)
            else:
                # print("Image found at {},{}".format(x,y))
                img_slice = image[xmin:-1, ymin:ymax]
                detection_list.append(img_slice)
        elif ymin < 0:
            # print("Image found at {},{}".format(x,y))
            img_slice = image[xmin:xmax, 0:ymax]
            detection_list.append(img_slice)
        elif ymax >= image.shape[1]:
            # print("Image found at {},{}".format(x,y))
            img_slice = image[xmin:xmax, ymin:-1]
            detection_list.append(img_slice)

    return detection_list


###
# Dilates images
###
def dilate(image):
    image = np.array(image)

    # Convert to float: Important for subtraction later which won't work with uint8
    image = img_as_float(image)
    image = gaussian_filter(image, 1)

    seed = np.copy(image)
    seed[1:-1, 1:-1] = image.min()
    mask = image

    dilated = reconstruction(seed, mask, method="dilation")
    newImg = image - dilated
    return newImg


###
# Download images from box
###
def download_images(folder_id, output_directory):

    client = Client(oauth)
    training_folder = client.folder(folder_id).get()
    training_images = training_folder.get_items()
    for img in training_images:
        img_file = client.file(file_id=img.id).get()
        with open(output_directory + img_file.name, "wb") as open_file:
            client.file(img_file.id).download_to(open_file)
            open_file.close()


###
# Create training set
###
def training_set(img_list, training_output_directory):
    train = []
    for i in range(len(img_list)):
        dilated = dilate(io.imread(img_list[i]))
        # threshold gets more images the smaller the number
        blobs_log = blob_log(dilated, max_sigma=50, num_sigma=5, threshold=0.06)
        # scaling is best at 10, min_offset zooms in and controls how many images are output, 8 is a good number
        a_list = extract_detections(dilated, blobs_log, min_offset=1, scaling=10)
        # plt.figure()

        for x in range(len(a_list)):
            # plt.figure()
            train.append(a_list[x])
            # plt.imshow(a_list[x], cmap="gray")
            training_output_path = f"{training_output_directory}image_split_{i}_{x}.tif"
            img = Image.fromarray(a_list[x])
            print(f"Saving image_split_{i}_{x}.tif")
            img.save(training_output_path)
    # plt.show()


###
# Reads in images and then flattens them into a dataframe
###


def flat_images(training_folder):
    images = io.ImageCollection(training_folder)
    flat_images = []
    for i in range(len(images)):
        img = images[i]
        img1 = img.flatten()
        flat_images.append(img1)
    df = pd.DataFrame(flat_images)
    return df


###
# Splits into train test and validation (in a format that deep learning can use)
###


def train_validation_test_split(training_folder, output_folder):
    split_folders.ratio(
        training_folder, output=output_folder, seed=1337, ratio=(0.8, 0.2)
    )
    return print("Complete")


def train_test_split(training_folder, output_folder):
    split_folders.ratio(
        training_folder, output=output_folder, seed=1337, ratio=(0.8, 0.1, 0.1)
    )
    return print("Complete")
