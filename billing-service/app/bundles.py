"""Unpacks invoice template bundles uploaded by admins."""

import io
import os
import tarfile


def unpack_bundle(data: bytes, dest: str) -> list[str]:
    """Extracts a .tar.gz bundle into dest, refusing links and paths outside dest."""
    root = os.path.realpath(dest)
    written = []
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tf:
        for member in tf.getmembers():
            if not (member.isfile() or member.isdir()):
                raise ValueError(f"refusing link or special file in bundle: {member.name}")
            target = os.path.realpath(os.path.join(root, member.name))
            if os.path.commonpath([root, target]) != root:
                raise ValueError(f"refusing path outside the bundle folder: {member.name}")
            if member.isfile():
                source = tf.extractfile(member)
                os.makedirs(os.path.dirname(target), exist_ok=True)
                with open(target, "wb") as out:
                    out.write(source.read() if source else b"")
                written.append(member.name)
    return written
