import { copyFileSync, mkdirSync, readFileSync } from "node:fs";

// The entry's post lives in POST.json; the house reads the post itself.
// This program only copies the file to /output, nothing else.
const post = JSON.parse(readFileSync("POST.json", "utf8"));
if (typeof post.url !== "string") {
  throw new Error("POST.json must be a JSON object with a string 'url'");
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync("POST.json", `${outDir}/POST.json`);
console.log("Copied POST.json to " + outDir);
