import yaml
import os
import argparse


class Loader(yaml.SafeLoader):

    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)


Loader.add_constructor('!include', Loader.include)

parser = argparse.ArgumentParser()
parser.add_argument('root_document', help='Root document')
parser.add_argument('-o', '--output-file', help='Path for your generated file. Default : out.yaml')


def main():
    args = parser.parse_args()

    with open(args.root_document, 'r') as f:
        doc = yaml.dump(yaml.load(f, Loader))

    if args.output_file:
        with open(args.output_file, 'w') as f:
            f.write(doc)
    else:
        print(doc)
