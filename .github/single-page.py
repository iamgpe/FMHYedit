import glob
import time


def output():
    read = glob.glob("*.md")
    content = ""
    nsfw_content = ""
    for file in read:
        if file != "README.md" or file != "feedback.md" or file != "posts.md":
            with open(file, "r") as f:
                if "NSFWPiracy.md" == file:
                    nsfw_content += f.read()
                    continue
                content += f.read()
    return content + nsfw_content


def main():
    content = output()
    with open("single-page", "w") as file:
        file.write(content)


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
