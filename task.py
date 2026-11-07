Page_size = 1024
Virtual_space = 4096  

page_table = {
    0: (2, True),
    1: (0, True),
    2: (3, True),
    3: (None, False),
}

def translate(address):
    vpn = address // Page_size
    offset = address % Page_size

    print(f"VPN = {vpn}")
    print(f"Offset = {offset}")

    frame, valid = page_table[vpn]

    if valid:
        physical_address = (frame * Page_size) + offset
        print(f"Frame = {frame}")
        print(f"Physical address = {physical_address}")
    else:
        print("PAGE FAULT")

def main():
    print("Virtual -> Physical address translation")
    print("Enter a virtual address (0-4095) or q to quit.\n")

    while True:
        text = input("Virtual address: ").strip()

        if text.lower() == "q":
            print("Goodbye!")
            break

        try:
            address = int(text)
        except ValueError:
            print("  Error: enter a number or q.\n")
            continue

        if address < 0:
            print("  Error: negative addresses are not allowed.\n")
            continue
        if address >= Virtual_space:
            print("  Error: address must be between 0 and 4095.\n")
            continue

        translate(address)
        print()

if __name__ == "__main__":
    main()