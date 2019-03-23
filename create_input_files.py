from utils import create_input_files
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create input files')

    parser.add_argument('--dataset', '-d', default='coco', help='dataset')
    parser.add_argument('--img_folder', '-i', default='image_folder', help='path to image')
    parser.add_argument('--caption_folder', '-cf', default='caption_datasets', help='path to captions')

    args = parser.parse_args()

    # Create input files (along with word map)
    create_input_files(dataset=args.dataset,
                       karpathy_json_path=os.path.join(args.caption_folder, 'dataset_{:s}.json'.format(args.dataset)),
                       image_folder=args.img_folder,
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='{:s}_folder'.format(args.dataset),
                       max_len=50)
