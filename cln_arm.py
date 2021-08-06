#!/usr/bin/env python3

import xmlrpc.client
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("invalid arguments to run client")
        print("should be './cln_arm <server_host>:<server_port>")
        sys.exit(1)

    urlEndPoint = f"http://{sys.argv[1]}"

    with xmlrpc.client.ServerProxy(urlEndPoint) as proxy:
        while True:
            cmd = input().split(",")

            # handles insert command
            if cmd[0] == "I" and len(cmd) == 4:
                print(proxy.insert(cmd[1], cmd[2], cmd[3]))
            # handles get/consult command
            elif cmd[0] == "C" and len(cmd) == 2:
                resp = proxy.get(cmd[1])
                # prints key's description and value, if key exists in database
                if resp != -1:
                    print(f"{resp[0]}, {resp[1]}")
                    continue
                # prints -1 otherwise
                print(resp)
            # handles terminate command and closes client
            elif cmd[0] == "T" and len(cmd) == 1:
                print(proxy.terminate())
                break
            else:
                print("invalid command")
