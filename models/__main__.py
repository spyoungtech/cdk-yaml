import time

if __name__ == '__main__':
    start = time.time()
    print('start', time.time())
    from . import MegaModel
    from contextlib import contextmanager
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--outfile', help='outfile', dest='out')
    parser.add_argument('-i', '--indent', help='indent', dest='indent', type=int, default=2)
    parser.add_argument('--compact', help='Generate with no whitespace. the indent flag is ignored when this is specified', action='store_true')
    parser.add_argument('--dry-run', help='Do not output anything', dest='dry_run', action='store_true')
    args = parser.parse_args()

    @contextmanager
    def increased_recursion_limit(n: int = 10000):
        old_limit = sys.getrecursionlimit()
        try:
            sys.setrecursionlimit(n)
            yield
        finally:
            sys.setrecursionlimit(old_limit)
    with increased_recursion_limit():
        schema = MegaModel.model_json_schema()
    end = time.time()
    print('end')
    import json
    if not args.dry_run:
        if args.out:
            with open(args.out, 'w') as f:
                if args.compact:
                    json.dump(schema, f, separators=(',',':'))
                else:
                    json.dump(schema, f, indent=args.indent)
        else:
            if args.compact:
                print(json.dumps(schema, separators=(',', ':')), end='')
            else:
                print(json.dumps(schema, indent=args.indent))

    print(end - start)
