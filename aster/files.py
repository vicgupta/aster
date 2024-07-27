class Files:
    def __init__(self) -> None:
        pass

    def read(self, filename: str):
        try:
            with open(filename, "r+", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print("Error reading file:", str(e))
            return False

    def save(self, filename: str, file_content: str):
        try:
            with open(filename, "w+", encoding="utf-8") as f:
                f.write(file_content)
            f.close()
            return True
        except Exception as e:
            print("Error saving file:", str(e))
            return False

    def append(self, filename: str, file_content: str):
        try:
            with open(filename, "a+", encoding="utf-8") as f:
                f.write(file_content)
            f.close()
            return True
        except Exception as e:
            print("Error appending to file:", str(e))
            return False


# def read_file (filename):
#     try:
#         with open(filename, 'r+', encoding='utf-8') as f:
#             return f.read()
#     except:
#             print ("Error reading file")
#             return False

# def save_file (filename, file_content):
#     try:
#         with open(filename, "w+", encoding='utf-8') as f:
#             f.write(file_content)
#         f.close()
#         return True
#     except Exception as e:
#         print("Error saving file:", str(e))
#         return False

# def append_file (filename, file_content):
#     try:
#         #with open(filename, "w+", encoding='utf-8') as f:
#         with open(filename, "a+", encoding='utf-8') as f:
#             f.write(file_content)
#         f.close()
#         return True
#     except:
#         print ("Error saving file")
#         return False
