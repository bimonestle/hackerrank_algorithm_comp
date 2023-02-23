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
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function timeConversion(s: string): string {
  // Write your code here
  const hour = s.slice(0, 2);
  let hourToNumber = Number(hour);

  const format = s.slice(8, 10);
  const rest = s.slice(2, 8);

  let newTime = `${hour}${rest}`;

  if (format === "AM" && hourToNumber >= 12) {
    hourToNumber = hourToNumber - 12;
    newTime = `0${hourToNumber}${rest}`;
  }

  if (format === "PM" && hourToNumber < 12) {
    hourToNumber = hourToNumber + 12;
    newTime = `${hourToNumber}${rest}`;
  }

  return newTime;
}

function main() {
  const ws: WriteStream = createWriteStream(process.env["OUTPUT_PATH"]);

  const s: string = readLine();

  const result: string = timeConversion(s);

  ws.write(result + "\n");

  ws.end();
}
