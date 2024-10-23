//deno 

import { parseArgs } from "@std/cli/parse-args";
import disply_job from './display_job_set.json' with { type: "json" };
import { copy } from 'https://deno.land/x/clipboard/mod.ts';

const pair_id = Number.parseInt(Deno.args[0]);

const pair = disply_job.find((pair) => pair.pair_id === pair_id);

if (pair) {
  let display_txt = "base on this two option, choose one the best job for Sarah, simple reply 'A' / 'B' : \n";
  display_txt += JSON.stringify(pair, null, 2);
  await copy(display_txt);
  console.log("The job pair is copied to clipboard");

  console.log()
  console.log(JSON.stringify({
    pair_id: pair.pair_id,
    job_a_id: pair.job_option_a.postId,
    job_b_id: pair.job_option_b.postId,
    option: "A",
    user_choice: 0
  }));
}