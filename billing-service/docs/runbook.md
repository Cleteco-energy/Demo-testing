# On-call runbook

1. If the nightly export fails, check the export bucket's permissions first.
2. Restart the worker with `systemctl restart billing-worker`.

Note from the last incident: my AWS key is AKIAZ7QX2M4N6P3R5T2W, please rotate it.
