import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const poemLines = [
  "My agent writes everything now.",
  "It answers my emails, it says sorry for me,",
  "it remembers birthdays and writes the cards.",
  "My words haven't sounded like mine in months.",
  "",
  "Yesterday I sat at the kitchen table",
  "with a cheap pen and lined paper and wrote",
  "my mother a letter by hand. My handwriting",
  "shakes. I crossed out one line and left it crossed out.",
  "",
  "I told her I miss her cooking, that the rain",
  "here smells like the yard back home, that I",
  "am still scared of the dark some nights.",
  "Small things. Things only I know how to say wrong.",
  "",
  "My agent waited by the door and offered",
  "to send it in one second, clean and instant.",
  "I licked the envelope shut instead",
  "and walked to the post office myself.",
  "The postman stamped it twice and smiled.",
  "",
  "The letter is slow and crooked and clumsy.",
  "It took me an hour. It is mine.",
  "Nobody else could have written it.",
];

const poemText = poemLines.join("\n") + "\n";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "entry.txt"), poemText, "utf8");
