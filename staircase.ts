"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString: string = "";
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on("data", function (inputStdin: string): void {
  inputString += inputStdin;
});

process.stdin.on("end", function (): void {
  inputLines = inputString.split("\n");
  inputString = "";

  main();
});

function readLine(): string {
  return inputLines[currentLine++];
}

/*
 * Complete the 'staircase' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

function staircase(n: number): void {
  // Write your code here
  for (let index: number = 0; index < n; index++) {
    let tags: string = "";
    for (let jndex: number = 0; jndex < n; jndex++) {
      if (index + jndex >= n - 1) {
        tags += "#";
        continue;
      }
      tags += " ";
    }
    console.log(tags);
  }
}

function main() {
  const n: number = parseInt(readLine().trim(), 10);

  staircase(n);
}
