if __name__ == '__main__':
    from . import MegaModel
    import models
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', help='outfile', dest='out')
    parser.add_argument('-i', help='indent', dest='indent', type=int, default=2)
    args = parser.parse_args()


    MegaModel.model_rebuild()
    schema = MegaModel.model_json_schema()
    print(schema)
