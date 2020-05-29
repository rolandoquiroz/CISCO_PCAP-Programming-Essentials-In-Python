#!/usr/bin/python3
"""
-Minimize the number of print() function invocations by inserting the \n
sequence into the strings
-Make the arrow twice as large (but keep the proportions)
-Duplicate the arrow, placing both arrows side by side;
"""
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
print("       *\n      * *\n     *   *\n    *     *\n   *       *\n"
      "  *         *\n *           *\n****       ****\n   *       *\n"
      "   *       *\n   *       *\n   *       *\n   *********")
print(2*"       *       ", 2*"      * *      ", 2*"     *   *     ",
      2*"    *     *    ", 2*"   *       *   ", 2*"  *         *  ",
      2*" *           * ", 2*"****       ****", 2*"   *       *   ",
      2*"   *       *   ", 2*"   *       *   ", 2*"   *       *   ",
      2*"   *********   ", sep='\n')
