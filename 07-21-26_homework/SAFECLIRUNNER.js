// runner.js — TODOs filled in
class ConfigError extends Error {
  constructor(message) {
    super(message);
    this.name = 'ConfigError';
  }
}

function loadThreshold() {
  // TODO 1: read process.env.MAX_ITEMS
  const raw = process.env.MAX_ITEMS;

  // TODO 2: if it's missing, throw a ConfigError
  if (raw === undefined) {
    throw new ConfigError('MAX_ITEMS environment variable is not set');
  }

  // TODO 3: otherwise return it as a Number
  const value = Number(raw);
  if (Number.isNaN(value)) {
    throw new ConfigError(`MAX_ITEMS is not a valid number: "${raw}"`);
  }
  return value;
}

async function run(items) {
  const limit = loadThreshold();
  if (items.length > limit) {
    throw new Error(`Too many items: ${items.length} > ${limit}`);
  }
  return items.map(i => i.toUpperCase());
}

const verbose = process.argv.includes('--verbose');

// TODO 4: wrap run([...]) in try/catch
(async () => {
  try {
    const result = await run(['apple', 'banana', 'cherry']);
    console.log(result);
  } catch (err) {
    // TODO 5: if verbose, console.log the full error stack; otherwise just err.message
    if (verbose) {
      console.error(err.stack);
    } else {
      console.error(err.message);
    }
    process.exitCode = 1;
  }
})();

// TODO 6: add a top-level process.on('unhandledRejection', ...) as a final safety net
process.on('unhandledRejection', (reason) => {
  if (verbose) {
    console.error('Unhandled rejection:', reason);
  } else {
    console.error('Unhandled rejection:', reason instanceof Error ? reason.message : reason);
  }
  process.exitCode = 1;
});