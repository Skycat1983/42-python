#!/usr/bin/env python3

# 'with' autimatically handles cleanup
# context manager is any object that knows how to set something up at
# start and stop something at the end


def secure_archive(
    filename: str,
    action: str = "r",
    content: str = "",
) -> tuple[bool, str]:
    return_value = ""
    status = False

    try:
        if action not in ("r", "w"):
            raise ValueError(f"Invalid action: {action}")

        with open(filename, action) as file:
            if action == "r":
                return_value = file.read()
            elif action == "w":
                file.write(content)
                return_value = "Content successfully written to file"
            status = True
    except ValueError as e:
        return_value = str(e)

    except PermissionError as e:
        return_value = str(e)
    except Exception as e:
        return_value = str(e)
    return (status, return_value)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===", end="\n\n")
    existing = "texts/fragment.txt"
    nonexisting = "texts/no_such_file.txt"
    private = "texts/no_read.txt"
    new_file = "texts/new_file.txt"
    read = "r"
    write = "w"
    print("Using 'secure_archive'to read from a nonexistent file:")
    print(secure_archive(nonexisting, read), end="\n\n")
    print("Using 'secure_archive'to read from an inaccessible file:")
    print(secure_archive(private, read), end="\n\n")
    print("Using 'secure_archive'to read from a regular file:")
    tuple_return = secure_archive(existing, read)
    print(tuple_return, end="\n\n")
    status, content = tuple_return
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive(new_file, write, content))


#  Using 'secure_archive'to read from a nonexistent file:
# (False, "[Errno 2] No such file or directory: '/not/existing/file'")
# Using 'secure_archive'to read from an inaccessible file:
# (False, "[Errno 13] Permission denied: '/etc/master.passwd'")
# Using 'secure_archive'to read from a regular file:
# (True, '[FRAGMENT 001] Digital preservation protocols established 2087\n'
# '[FRAGMENT 002] Knowledge must survive the entropy wars\n'
# '[FRAGMENT 003] Every byte saved is a victory against oblivion\n')
# Using 'secure_archive'to write previous content to a new file:
# (True, 'Content successfully written to file')
