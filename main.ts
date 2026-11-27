// news-image-20261127 — entrypoint (Node 22, stdlib only).
//
// The poster itself is drawn by build_image.py and kept in this
// repository as entry.png: a split-flap airport departure board,
// "WORLD DEPARTURES — FRI 27 NOV 2026". The hero row is the Kuwait
// drone strike that killed 2 Italians, which Iran denies; the other
// rows carry Gaza, the Thanksgiving storm, Mali, the France vote,
// the Ibiza tanker and UK migration. This program's only job is to
// place that exact image at /output/entry.png, byte for byte, so
// every run writes the same bytes. Nothing here reads the network
// or the clock.

import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const target = "/output/entry.png";

mkdirSync(dirname(target), { recursive: true });
copyFileSync(source, target);
const bytes = statSync(target).size;
console.log(`wrote ${target} (${bytes} bytes)`);
