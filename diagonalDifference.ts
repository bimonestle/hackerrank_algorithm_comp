"use strict";

import { WriteStream, createWriteStream } from "fs";
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
 * Complete the 'diagonalDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

function diagonalDifference(arr: number[][]): number {
  // Write your code here
  let leftDiagonal: number = 0;
  let rightDiagonal: number = 0;

  for (let firstIndex: number = 0; arr.length; firstIndex++) {
    for (let secondIndex: number = 0; arr.length; secondIndex++) {
      if (firstIndex === secondIndex) {
        leftDiagonal += arr[firstIndex][secondIndex];
        continue;
      }

      if (firstIndex + secondIndex === arr.length - 1) {
        rightDiagonal += arr[firstIndex][secondIndex];
        continue;
      }
    }
  }

  const result: number = Math.abs(leftDiagonal - rightDiagonal);

  return result;
}

function main() {
  const ws: WriteStream = createWriteStream(process.env["OUTPUT_PATH"]);

  const n: number = parseInt(readLine().trim(), 10);

  let arr: number[][] = Array(n);

  for (let i: number = 0; i < n; i++) {
    arr[i] = readLine()
      .replace(/\s+$/g, "")
      .split(" ")
      .map((arrTemp) => parseInt(arrTemp, 10));
  }

  const result: number = diagonalDifference(arr);

  ws.write(result + "\n");

  ws.end();
}
