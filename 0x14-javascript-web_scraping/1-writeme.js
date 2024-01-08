#!/usr/bin/node

import { writeFile } from 'fs';
const data = process.argv[1];
const filename = process.argv[2];
writeFile(data, filename, 'utf-8', (err) => {
  if (err) throw err;
});
