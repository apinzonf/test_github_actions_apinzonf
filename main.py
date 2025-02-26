import argparse

def main():
    parser = argparse.ArgumentParser(description="Greet Alex with a custom input name.")
    parser.add_argument("name", type=str, help="The name to be greeted")
    args = parser.parse_args()
    
    print(f"Hello {args.name}")

if __name__ == "__main__":
    main()
