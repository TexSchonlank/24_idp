#!/bin/python

# Copyright 2024 Tex Schönlank

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version. This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details. You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import sys

stack = []

def main():

    # when stack contains one element, that is the final value
    while len(stack) > 1:

        # internalize our stack frame
        returnvalue = stack[-1]
        pc = stack[-2]
        n = stack[-3]
        m = stack[-4]

        # increase our program counter
        stack[-2] += 1

        # determine which case of the function by parts we are in
        if m == 0:
            # case 1
            # remove our stack frame
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            # put the correct value in the returnvalue below
            stack[-1] = n+1

        elif n == 0:
            # case 2

            if pc == 0:
                # we must run A(m-1, 1)
                stack.append(m-1)
                stack.append(1)
                stack.append(0)
                stack.append(None)

            elif pc == 1:
                # we just ran A(m-1, 1) and must report the returnvalue
                # remove our stack frame
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                # put the correct value in the returnvalue below
                stack[-1] = returnvalue

            else:
                print("error: pc == 2 in case 2")
                return

        else:
            # case 3

            if pc == 0:
                # we must run A(m, n-1)
                stack.append(m)
                stack.append(n-1)
                stack.append(0)
                stack.append(None)

            elif pc == 1:
                # we just ran A(m, n-1) and must use it to run A(m-1, A(m, n-1))
                stack.append(m-1)
                stack.append(returnvalue)
                stack.append(0)
                stack.append(None)

            elif pc == 2:
                # we just ran A(m-1, A(m, n-1)) and must report the returnvalue
                # remove our stack frame
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                # put the correct value in the returnvalue below
                stack[-1] = returnvalue

            else:
                print("error: pc == 2 in case 3")
                return

    final = stack.pop()
    print(final)

if __name__ == "__main__":
    m = None
    n = None
    try:
        m = int(sys.argv[1])
        n = int(sys.argv[2])
    except: 
        print("Could not read two integers")
        quit()

    if m < 0 or n < 0:
        print("Arguments should be at least 0")
        quit()

    # the final return value
    stack.append(None)

    # the first stack frame
    stack.append(m)
    stack.append(n)
    stack.append(0)
    stack.append(None)

    #run the loop
    main()
