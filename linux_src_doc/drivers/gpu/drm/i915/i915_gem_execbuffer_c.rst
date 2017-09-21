.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_execbuffer.c

.. _`user-command-execution`:

User command execution
======================

Userspace submits commands to be executed on the GPU as an instruction
stream within a GEM object we call a batchbuffer. This instructions may
refer to other GEM objects containing auxiliary state such as kernels,
samplers, render targets and even secondary batchbuffers. Userspace does
not know where in the GPU memory these objects reside and so before the
batchbuffer is passed to the GPU for execution, those addresses in the
batchbuffer and auxiliary objects are updated. This is known as relocation,
or patching. To try and avoid having to relocate each object on the next
execution, userspace is told the location of those objects in this pass,
but this remains just a hint as the kernel may choose a new location for
any object in the future.

Processing an execbuf ioctl is conceptually split up into a few phases.

1. Validation - Ensure all the pointers, handles and flags are valid.
2. Reservation - Assign GPU address space for every object
3. Relocation - Update any addresses to point to the final locations
4. Serialisation - Order the request with respect to its dependencies
5. Construction - Construct a request to execute the batchbuffer
6. Submission (at some point in the future execution)

Reserving resources for the execbuf is the most complicated phase. We
neither want to have to migrate the object in the address space, nor do
we want to have to update any relocations pointing to this object. Ideally,
we want to leave the object where it is and for all the existing relocations
to match. If the object is given a new address, or if userspace thinks the
object is elsewhere, we have to parse all the relocation entries and update
the addresses. Userspace can set the I915_EXEC_NORELOC flag to hint that
all the target addresses in all of its objects match the value in the
relocation entries and that they all match the presumed offsets given by the
list of execbuffer objects. Using this knowledge, we know that if we haven't
moved any buffers, all the relocation entries are valid and we can skip
the update. (If userspace is wrong, the likely outcome is an impromptu GPU
hang.) The requirement for using I915_EXEC_NO_RELOC are:

The addresses written in the objects must match the corresponding
reloc.presumed_offset which in turn must match the corresponding
execobject.offset.

Any render targets written to in the batch must be flagged with
EXEC_OBJECT_WRITE.

To avoid stalling, execobject.offset should match the current
address of that object within the active context.

The reservation is done is multiple phases. First we try and keep any
object already bound in its current location - so as long as meets the
constraints imposed by the new execbuffer. Any object left unbound after the
first pass is then fitted into any available idle space. If an object does
not fit, all objects are removed from the reservation and the process rerun
after sorting the objects into a priority order (more difficult to fit
objects are tried first). Failing that, the entire VM is cleared and we try
to fit the execbuf once last time before concluding that it simply will not
fit.

A small complication to all of this is that we allow userspace not only to
specify an alignment and a size for the object in the address space, but
we also allow userspace to specify the exact offset. This objects are
simpler to place (the location is known a priori) all we have to do is make
sure the space is available.

Once all the objects are in place, patching up the buried pointers to point
to the final locations is a fairly simple job of walking over the relocation
entry arrays, looking up the right address and rewriting the value into
the object. Simple! ... The relocation entries are stored in user memory
and so to access them we have to copy them into a local buffer. That copy
has to avoid taking any pagefaults as they may lead back to a GEM object
requiring the struct_mutex (i.e. recursive deadlock). So once again we split
the relocation into multiple passes. First we try to do everything within an
atomic context (avoid the pagefaults) which requires that we never wait. If
we detect that we may wait, or if we need to fault, then we have to fallback
to a slower path. The slowpath has to drop the mutex. (Can you hear alarm
bells yet?) Dropping the mutex means that we lose all the state we have
built up so far for the execbuf and we must reset any global data. However,
we do leave the objects pinned in their final locations - which is a
potential issue for concurrent execbufs. Once we have left the mutex, we can
allocate and copy all the relocation entries into a large array at our
leisure, reacquire the mutex, reclaim all the objects and other state and
then proceed to update any incorrect addresses with the objects.

As we process the relocation entries, we maintain a record of whether the
object is being written to. Using NORELOC, we expect userspace to provide
this information instead. We also check whether we can skip the relocation
by comparing the expected value inside the relocation entry with the target's
final address. If they differ, we have to map the current object and rewrite
the 4 or 8 byte pointer within.

Serialising an execbuf is quite simple according to the rules of the GEM
ABI. Execution within each context is ordered by the order of submission.
Writes to any GEM object are in order of submission and are exclusive. Reads
from a GEM object are unordered with respect to other reads, but ordered by
writes. A write submitted after a read cannot occur before the read, and
similarly any read submitted after a write cannot occur before the write.
Writes are ordered between engines such that only one write occurs at any
time (completing any reads beforehand) - using semaphores where available
and CPU serialisation otherwise. Other GEM access obey the same rules, any
write (either via mmaps using set-domain, or via pwrite) must flush all GPU
reads before starting, and any read (either using set-domain or pread) must
flush all GPU writes before starting. (Note we only employ a barrier before,
we currently rely on userspace not concurrently starting a new execution
whilst reading or writing to an object. This may be an advantage or not
depending on how much you trust userspace not to shoot themselves in the
foot.) Serialisation may just result in the request being inserted into
a DAG awaiting its turn, but most simple is to wait on the CPU until
all dependencies are resolved.

After all of that, is just a matter of closing the request and handing it to
the hardware (well, leaving it in a queue to be executed). However, we also
offer the ability for batchbuffers to be run with elevated privileges so
that they access otherwise hidden registers. (Used to adjust L3 cache etc.)
Before any batch is given extra privileges we first must check that it
contains no nefarious instructions, we check that each instruction is from
our whitelist and all registers are also from an allowed list. We first
copy the user's batchbuffer to a shadow (so that the user doesn't have
access to it, either by the CPU or GPU as we scan it) and then parse each
instruction. If everything is ok, we set a flag telling the hardware to run
the batchbuffer in trusted mode, otherwise the ioctl is rejected.

.. _`gen8_dispatch_bsd_engine`:

gen8_dispatch_bsd_engine
========================

.. c:function:: unsigned int gen8_dispatch_bsd_engine(struct drm_i915_private *dev_priv, struct drm_file *file)

    The engine index is returned.

    :param struct drm_i915_private \*dev_priv:
        *undescribed*

    :param struct drm_file \*file:
        *undescribed*

.. This file was automatic generated / don't edit.

