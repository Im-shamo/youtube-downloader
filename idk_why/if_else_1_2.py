def main():
    N = 2000
    output = ["ans = int(input('Enter a number\\n>'))\n", "def why(ans):\n", "\tif ans == 0:\n", "\t\tprint('even')\n"]

    for i in range(1, N):
        if i % 2 == 0:
            output.extend([f"\telif ans == {i}:\n", f"\t\tprint('even')\n"])
        else:
            output.extend([f"\telif ans == {i}:\n", f"\t\tprint('odd')\n"])

    # for line in output:
    #     print(line)
    output.append("why(ans)")

    with open("output/dont/output.py", "w") as file:
        file.writelines(output)

if __name__ == "__main__":
    main()
