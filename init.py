import os

def create_env_file():

    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write("TOKEN=your_token_here\n")
    else:
        print(".env файл уже существует.")

if __name__ == "__main__":
    create_env_file()