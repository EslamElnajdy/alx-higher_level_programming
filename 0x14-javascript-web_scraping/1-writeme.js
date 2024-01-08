#!/usr/bin/node

import { writeFile } from 'fs';
const data = process.argv[2];
const filename = process.argv[3];
writeFile(filename, data, 'utf-8', (err) => {
  if (err) throw err;
});
