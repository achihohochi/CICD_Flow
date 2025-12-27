const test = require("node:test");
const assert = require("node:assert/strict");
const { add } = require("./math");

test("add works", () => {
  assert.equal(add(2, 3), 5);
});
