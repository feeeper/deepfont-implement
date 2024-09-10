from pathlib import Path
from argparse import ArgumentParser
import shutil


def main(input_path: Path, output_path: Path, size: int) -> None:
    if output_path.exists():
        shutil.rmtree(output_path)
    
    output_path.mkdir(parents=True)
    for dir in input_path.iterdir():
        class_output_dir = output_path / dir.name
        if class_output_dir.exists():
            shutil.rmtree(class_output_dir)

        class_output_dir.mkdir(parents=True)
        for i, file in enumerate(dir.iterdir()):            
            shutil.copy(file, class_output_dir / file.name)
            if i == size - 1:
                break

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_path', '-i', type=Path, required=True, default='train_data/')
    parser.add_argument('--output_path', '-o', type=Path, required=True, default='train_data_subset/')
    parser.add_argument('--size', '-s', type=int, default=100)
    args = parser.parse_args()
    main(args.input_path, args.output_path, args.size)
