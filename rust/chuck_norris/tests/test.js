const assert = require('node:assert/strict');
const ck = require('../pkg/chuck_norris.js');

const actual = ck.get_fact()
console.dir(ck.__wasm);
assert.ok(actual.includes("Chuck Norris"))
