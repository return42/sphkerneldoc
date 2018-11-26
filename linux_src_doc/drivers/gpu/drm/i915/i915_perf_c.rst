.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_perf.c

.. _`i915-perf-overview`:

i915 Perf Overview
==================

Gen graphics supports a large number of performance counters that can help
driver and application developers understand and optimize their use of the
GPU.

This i915 perf interface enables userspace to configure and open a file
descriptor representing a stream of GPU metrics which can then be \ :c:func:`read`\  as
a stream of sample records.

The interface is particularly suited to exposing buffered metrics that are
captured by DMA from the GPU, unsynchronized with and unrelated to the CPU.

Streams representing a single context are accessible to applications with a
corresponding drm file descriptor, such that OpenGL can use the interface
without special privileges. Access to system-wide metrics requires root
privileges by default, unless changed via the dev.i915.perf_event_paranoid
sysctl option.

.. _`i915-perf-history-and-comparison-with-core-perf`:

i915 Perf History and Comparison with Core Perf
===============================================

The interface was initially inspired by the core Perf infrastructure but
some notable differences are:

i915 perf file descriptors represent a "stream" instead of an "event"; where
a perf event primarily corresponds to a single 64bit value, while a stream
might sample sets of tightly-coupled counters, depending on the
configuration.  For example the Gen OA unit isn't designed to support
orthogonal configurations of individual counters; it's configured for a set
of related counters. Samples for an i915 perf stream capturing OA metrics
will include a set of counter values packed in a compact HW specific format.
The OA unit supports a number of different packing formats which can be
selected by the user opening the stream. Perf has support for grouping
events, but each event in the group is configured, validated and
authenticated individually with separate system calls.

i915 perf stream configurations are provided as an array of u64 (key,value)
pairs, instead of a fixed struct with multiple miscellaneous config members,
interleaved with event-type specific members.

i915 perf doesn't support exposing metrics via an mmap'd circular buffer.
The supported metrics are being written to memory by the GPU unsynchronized
with the CPU, using HW specific packing formats for counter sets. Sometimes
the constraints on HW configuration require reports to be filtered before it
would be acceptable to expose them to unprivileged applications - to hide
the metrics of other processes/contexts. For these use cases a \ :c:func:`read`\  based
interface is a good fit, and provides an opportunity to filter data as it
gets copied from the GPU mapped buffers to userspace buffers.


Issues hit with first prototype based on Core Perf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first prototype of this driver was based on the core perf
infrastructure, and while we did make that mostly work, with some changes to
perf, we found we were breaking or working around too many assumptions baked
into perf's currently cpu centric design.

In the end we didn't see a clear benefit to making perf's implementation and
interface more complex by changing design assumptions while we knew we still
wouldn't be able to use any existing perf based userspace tools.

Also considering the Gen specific nature of the Observability hardware and
how userspace will sometimes need to combine i915 perf OA metrics with
side-band OA data captured via MI_REPORT_PERF_COUNT commands; we're
expecting the interface to be used by a platform specific userspace such as
OpenGL or tools. This is to say; we aren't inherently missing out on having
a standard vendor/architecture agnostic interface by not using perf.


For posterity, in case we might re-visit trying to adapt core perf to be
better suited to exposing i915 metrics these were the main pain points we
hit:

- The perf based OA PMU driver broke some significant design assumptions:

  Existing perf pmus are used for profiling work on a cpu and we were
  introducing the idea of _IS_DEVICE pmus with different security
  implications, the need to fake cpu-related data (such as user/kernel
  registers) to fit with perf's current design, and adding _DEVICE records
  as a way to forward device-specific status records.

  The OA unit writes reports of counters into a circular buffer, without
  involvement from the CPU, making our PMU driver the first of a kind.

  Given the way we were periodically forward data from the GPU-mapped, OA
  buffer to perf's buffer, those bursts of sample writes looked to perf like
  we were sampling too fast and so we had to subvert its throttling checks.

  Perf supports groups of counters and allows those to be read via
  transactions internally but transactions currently seem designed to be
  explicitly initiated from the cpu (say in response to a userspace \ :c:func:`read`\ )
  and while we could pull a report out of the OA buffer we can't
  trigger a report from the cpu on demand.

  Related to being report based; the OA counters are configured in HW as a
  set while perf generally expects counter configurations to be orthogonal.
  Although counters can be associated with a group leader as they are
  opened, there's no clear precedent for being able to provide group-wide
  configuration attributes (for example we want to let userspace choose the
  OA unit report format used to capture all counters in a set, or specify a
  GPU context to filter metrics on). We avoided using perf's grouping
  feature and forwarded OA reports to userspace via perf's 'raw' sample
  field. This suited our userspace well considering how coupled the counters
  are when dealing with normalizing. It would be inconvenient to split
  counters up into separate events, only to require userspace to recombine
  them. For Mesa it's also convenient to be forwarded raw, periodic reports
  for combining with the side-band raw reports it captures using
  MI_REPORT_PERF_COUNT commands.

  - As a side note on perf's grouping feature; there was also some concern
    that using PERF_FORMAT_GROUP as a way to pack together counter values
    would quite drastically inflate our sample sizes, which would likely
    lower the effective sampling resolutions we could use when the available
    memory bandwidth is limited.

    With the OA unit's report formats, counters are packed together as 32
    or 40bit values, with the largest report size being 256 bytes.

    PERF_FORMAT_GROUP values are 64bit, but there doesn't appear to be a
    documented ordering to the values, implying PERF_FORMAT_ID must also be
    used to add a 64bit ID before each value; giving 16 bytes per counter.

  Related to counter orthogonality; we can't time share the OA unit, while
  event scheduling is a central design idea within perf for allowing
  userspace to open + enable more events than can be configured in HW at any
  one time.  The OA unit is not designed to allow re-configuration while in
  use. We can't reconfigure the OA unit without losing internal OA unit
  state which we can't access explicitly to save and restore. Reconfiguring
  the OA unit is also relatively slow, involving ~100 register writes. From
  userspace Mesa also depends on a stable OA configuration when emitting
  MI_REPORT_PERF_COUNT commands and importantly the OA unit can't be
  disabled while there are outstanding MI_RPC commands lest we hang the
  command streamer.

  The contents of sample records aren't extensible by device drivers (i.e.
  the sample_type bits). As an example; Sourab Gupta had been looking to
  attach GPU timestamps to our OA samples. We were shoehorning OA reports
  into sample records by using the 'raw' field, but it's tricky to pack more
  than one thing into this field because events/core.c currently only lets a
  pmu give a single raw data pointer plus len which will be copied into the
  ring buffer. To include more than the OA report we'd have to copy the
  report into an intermediate larger buffer. I'd been considering allowing a
  vector of data+len values to be specified for copying the raw data, but
  it felt like a kludge to being using the raw field for this purpose.

- It felt like our perf based PMU was making some technical compromises
  just for the sake of using perf:

  \ :c:func:`perf_event_open`\  requires events to either relate to a pid or a specific
  cpu core, while our device pmu related to neither.  Events opened with a
  pid will be automatically enabled/disabled according to the scheduling of
  that process - so not appropriate for us. When an event is related to a
  cpu id, perf ensures pmu methods will be invoked via an inter process
  interrupt on that core. To avoid invasive changes our userspace opened OA
  perf events for a specific cpu. This was workable but it meant the
  majority of the OA driver ran in atomic context, including all OA report
  forwarding, which wasn't really necessary in our case and seems to make
  our locking requirements somewhat complex as we handled the interaction
  with the rest of the i915 driver.

.. _`oa-tail-pointer-race`:

OA Tail Pointer Race
====================

There's a HW race condition between OA unit tail pointer register updates and
writes to memory whereby the tail pointer can sometimes get ahead of what's
been written out to the OA buffer so far (in terms of what's visible to the
CPU).

Although this can be observed explicitly while copying reports to userspace
by checking for a zeroed report-id field in tail reports, we want to account
for this earlier, as part of the oa_buffer_check to avoid lots of redundant
\ :c:func:`read`\  attempts.

In effect we define a tail pointer for reading that lags the real tail
pointer by at least \ ``OA_TAIL_MARGIN_NSEC``\  nanoseconds, which gives enough
time for the corresponding reports to become visible to the CPU.

To manage this we actually track two tail pointers:
 1) An 'aging' tail with an associated timestamp that is tracked until we
    can trust the corresponding data is visible to the CPU; at which point
    it is considered 'aged'.
 2) An 'aged' tail that can be used for \ :c:func:`read`\ ing.

The two separate pointers let us decouple \ :c:func:`read`\ s from tail pointer aging.

The tail pointers are checked and updated at a limited rate within a hrtimer
callback (the same callback that is used for delivering EPOLLIN events)

Initially the tails are marked invalid with \ ``INVALID_TAIL_PTR``\  which
indicates that an updated tail pointer is needed.

Most of the implementation details for this workaround are in
\ :c:func:`oa_buffer_check_unlocked`\  and \ :c:func:`_append_oa_reports`\ 

Note for posterity: previously the driver used to define an effective tail
pointer that lagged the real pointer by a 'tail margin' measured in bytes
derived from \ ``OA_TAIL_MARGIN_NSEC``\  and the configured sampling frequency.
This was flawed considering that the OA unit may also automatically generate
non-periodic reports (such as on context switch) or the OA unit may be
enabled without any periodic sampling.

.. _`perf_open_properties`:

struct perf_open_properties
===========================

.. c:type:: struct perf_open_properties

    for validated properties given to open a stream

.. _`perf_open_properties.definition`:

Definition
----------

.. code-block:: c

    struct perf_open_properties {
        u32 sample_flags;
        u64 single_context:1;
        u64 ctx_handle;
        int metrics_set;
        int oa_format;
        bool oa_periodic;
        int oa_period_exponent;
    }

.. _`perf_open_properties.members`:

Members
-------

sample_flags
    `DRM_I915_PERF_PROP_SAMPLE_*` properties are tracked as flags

single_context
    Whether a single or all gpu contexts should be monitored

ctx_handle
    A gem ctx handle for use with \ ``single_context``\ 

metrics_set
    An ID for an OA unit metric set advertised via sysfs

oa_format
    An OA unit HW report format

oa_periodic
    Whether to enable periodic OA unit sampling

oa_period_exponent
    The OA unit sampling period is derived from this

.. _`perf_open_properties.description`:

Description
-----------

As \ :c:func:`read_properties_unlocked`\  enumerates and validates the properties given
to open a stream of metrics the configuration is built up in the structure
which starts out zero initialized.

.. _`oa_buffer_check_unlocked`:

oa_buffer_check_unlocked
========================

.. c:function:: bool oa_buffer_check_unlocked(struct drm_i915_private *dev_priv)

    check for data and update tail ptr state

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`oa_buffer_check_unlocked.description`:

Description
-----------

This is either called via fops (for blocking reads in user ctx) or the poll
check hrtimer (atomic ctx) to check the OA buffer tail pointer and check
if there is data available for userspace to read.

This function is central to providing a workaround for the OA unit tail
pointer having a race with respect to what data is visible to the CPU.
It is responsible for reading tail pointers from the hardware and giving
the pointers time to 'age' before they are made available for reading.
(See description of OA_TAIL_MARGIN_NSEC above for further details.)

Besides returning true when there is data available to \ :c:func:`read`\  this function
also has the side effect of updating the oa_buffer.tails[], .aging_timestamp
and .aged_tail_idx state used for reading.

.. _`oa_buffer_check_unlocked.note`:

Note
----

It's safe to read OA config state here unlocked, assuming that this is
only called while the stream is enabled, while the global OA configuration
can't be modified.

.. _`oa_buffer_check_unlocked.return`:

Return
------

\ ``true``\  if the OA buffer contains data, else \ ``false``\ 

.. _`append_oa_status`:

append_oa_status
================

.. c:function:: int append_oa_status(struct i915_perf_stream *stream, char __user *buf, size_t count, size_t *offset, enum drm_i915_perf_record_type type)

    Appends a status record to a userspace \ :c:func:`read`\  buffer.

    :param stream:
        An i915-perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

    :param buf:
        destination buffer given by userspace
    :type buf: char __user \*

    :param count:
        the number of bytes userspace wants to read
    :type count: size_t

    :param offset:
        (inout): the current position for writing into \ ``buf``\ 
    :type offset: size_t \*

    :param type:
        The kind of status to report to userspace
    :type type: enum drm_i915_perf_record_type

.. _`append_oa_status.description`:

Description
-----------

Writes a status record (such as `DRM_I915_PERF_RECORD_OA_REPORT_LOST`)
into the userspace \ :c:func:`read`\  buffer.

The \ ``buf``\  \ ``offset``\  will only be updated on success.

.. _`append_oa_status.return`:

Return
------

0 on success, negative error code on failure.

.. _`append_oa_sample`:

append_oa_sample
================

.. c:function:: int append_oa_sample(struct i915_perf_stream *stream, char __user *buf, size_t count, size_t *offset, const u8 *report)

    Copies single OA report into userspace \ :c:func:`read`\  buffer.

    :param stream:
        An i915-perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

    :param buf:
        destination buffer given by userspace
    :type buf: char __user \*

    :param count:
        the number of bytes userspace wants to read
    :type count: size_t

    :param offset:
        (inout): the current position for writing into \ ``buf``\ 
    :type offset: size_t \*

    :param report:
        A single OA report to (optionally) include as part of the sample
    :type report: const u8 \*

.. _`append_oa_sample.description`:

Description
-----------

The contents of a sample are configured through `DRM_I915_PERF_PROP_SAMPLE_*`
properties when opening a stream, tracked as `stream->sample_flags`. This
function copies the requested components of a single sample to the given
\ :c:func:`read`\  \ ``buf``\ .

The \ ``buf``\  \ ``offset``\  will only be updated on success.

.. _`append_oa_sample.return`:

Return
------

0 on success, negative error code on failure.

.. _`gen8_append_oa_reports`:

gen8_append_oa_reports
======================

.. c:function:: int gen8_append_oa_reports(struct i915_perf_stream *stream, char __user *buf, size_t count, size_t *offset)

    :param stream:
        An i915-perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

    :param buf:
        destination buffer given by userspace
    :type buf: char __user \*

    :param count:
        the number of bytes userspace wants to read
    :type count: size_t

    :param offset:
        (inout): the current position for writing into \ ``buf``\ 
    :type offset: size_t \*

.. _`gen8_append_oa_reports.description`:

Description
-----------

Notably any error condition resulting in a short read (-%ENOSPC or
-%EFAULT) will be returned even though one or more records may
have been successfully copied. In this case it's up to the caller
to decide if the error should be squashed before returning to
userspace.

.. _`gen8_append_oa_reports.note`:

Note
----

reports are consumed from the head, and appended to the
tail, so the tail chases the head?... If you think that's mad
and back-to-front you're not alone, but this follows the
Gen PRM naming convention.

.. _`gen8_append_oa_reports.return`:

Return
------

0 on success, negative error code on failure.

.. _`gen8_oa_read`:

gen8_oa_read
============

.. c:function:: int gen8_oa_read(struct i915_perf_stream *stream, char __user *buf, size_t count, size_t *offset)

    copy status records then buffered OA reports

    :param stream:
        An i915-perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

    :param buf:
        destination buffer given by userspace
    :type buf: char __user \*

    :param count:
        the number of bytes userspace wants to read
    :type count: size_t

    :param offset:
        (inout): the current position for writing into \ ``buf``\ 
    :type offset: size_t \*

.. _`gen8_oa_read.description`:

Description
-----------

Checks OA unit status registers and if necessary appends corresponding
status records for userspace (such as for a buffer full condition) and then
initiate appending any buffered OA reports.

Updates \ ``offset``\  according to the number of bytes successfully copied into
the userspace buffer.

NB: some data may be successfully copied to the userspace buffer
even if an error is returned, and this is reflected in the
updated \ ``offset``\ .

.. _`gen8_oa_read.return`:

Return
------

zero on success or a negative error code

.. _`gen7_append_oa_reports`:

gen7_append_oa_reports
======================

.. c:function:: int gen7_append_oa_reports(struct i915_perf_stream *stream, char __user *buf, size_t count, size_t *offset)

    :param stream:
        An i915-perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

    :param buf:
        destination buffer given by userspace
    :type buf: char __user \*

    :param count:
        the number of bytes userspace wants to read
    :type count: size_t

    :param offset:
        (inout): the current position for writing into \ ``buf``\ 
    :type offset: size_t \*

.. _`gen7_append_oa_reports.description`:

Description
-----------

Notably any error condition resulting in a short read (-%ENOSPC or
-%EFAULT) will be returned even though one or more records may
have been successfully copied. In this case it's up to the caller
to decide if the error should be squashed before returning to
userspace.

.. _`gen7_append_oa_reports.note`:

Note
----

reports are consumed from the head, and appended to the
tail, so the tail chases the head?... If you think that's mad
and back-to-front you're not alone, but this follows the
Gen PRM naming convention.

.. _`gen7_append_oa_reports.return`:

Return
------

0 on success, negative error code on failure.

.. _`gen7_oa_read`:

gen7_oa_read
============

.. c:function:: int gen7_oa_read(struct i915_perf_stream *stream, char __user *buf, size_t count, size_t *offset)

    copy status records then buffered OA reports

    :param stream:
        An i915-perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

    :param buf:
        destination buffer given by userspace
    :type buf: char __user \*

    :param count:
        the number of bytes userspace wants to read
    :type count: size_t

    :param offset:
        (inout): the current position for writing into \ ``buf``\ 
    :type offset: size_t \*

.. _`gen7_oa_read.description`:

Description
-----------

Checks Gen 7 specific OA unit status registers and if necessary appends
corresponding status records for userspace (such as for a buffer full
condition) and then initiate appending any buffered OA reports.

Updates \ ``offset``\  according to the number of bytes successfully copied into
the userspace buffer.

.. _`gen7_oa_read.return`:

Return
------

zero on success or a negative error code

.. _`i915_oa_wait_unlocked`:

i915_oa_wait_unlocked
=====================

.. c:function:: int i915_oa_wait_unlocked(struct i915_perf_stream *stream)

    handles blocking IO until OA data available

    :param stream:
        An i915-perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

.. _`i915_oa_wait_unlocked.description`:

Description
-----------

Called when userspace tries to \ :c:func:`read`\  from a blocking stream FD opened
for OA metrics. It waits until the hrtimer callback finds a non-empty
OA buffer and wakes us.

.. _`i915_oa_wait_unlocked.note`:

Note
----

it's acceptable to have this return with some false positives
since any subsequent read handling will return -EAGAIN if there isn't
really data ready for userspace yet.

.. _`i915_oa_wait_unlocked.return`:

Return
------

zero on success or a negative error code

.. _`i915_oa_poll_wait`:

i915_oa_poll_wait
=================

.. c:function:: void i915_oa_poll_wait(struct i915_perf_stream *stream, struct file *file, poll_table *wait)

    call \ :c:func:`poll_wait`\  for an OA stream \ :c:func:`poll`\ 

    :param stream:
        An i915-perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

    :param file:
        An i915 perf stream file
    :type file: struct file \*

    :param wait:
        \ :c:func:`poll`\  state table
    :type wait: poll_table \*

.. _`i915_oa_poll_wait.description`:

Description
-----------

For handling userspace polling on an i915 perf stream opened for OA metrics,
this starts a poll_wait with the wait queue that our hrtimer callback wakes
when it sees data ready to read in the circular OA buffer.

.. _`i915_oa_read`:

i915_oa_read
============

.. c:function:: int i915_oa_read(struct i915_perf_stream *stream, char __user *buf, size_t count, size_t *offset)

    just calls through to \ :c:type:`i915_oa_ops->read <i915_oa_ops>`\ 

    :param stream:
        An i915-perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

    :param buf:
        destination buffer given by userspace
    :type buf: char __user \*

    :param count:
        the number of bytes userspace wants to read
    :type count: size_t

    :param offset:
        (inout): the current position for writing into \ ``buf``\ 
    :type offset: size_t \*

.. _`i915_oa_read.description`:

Description
-----------

Updates \ ``offset``\  according to the number of bytes successfully copied into
the userspace buffer.

.. _`i915_oa_read.return`:

Return
------

zero on success or a negative error code

.. _`oa_get_render_ctx_id`:

oa_get_render_ctx_id
====================

.. c:function:: int oa_get_render_ctx_id(struct i915_perf_stream *stream)

    determine and hold ctx hw id

    :param stream:
        An i915-perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

.. _`oa_get_render_ctx_id.description`:

Description
-----------

Determine the render context hw id, and ensure it remains fixed for the
lifetime of the stream. This ensures that we don't have to worry about
updating the context ID in OACONTROL on the fly.

.. _`oa_get_render_ctx_id.return`:

Return
------

zero on success or a negative error code

.. _`oa_put_render_ctx_id`:

oa_put_render_ctx_id
====================

.. c:function:: void oa_put_render_ctx_id(struct i915_perf_stream *stream)

    counterpart to oa_get_render_ctx_id releases hold

    :param stream:
        An i915-perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

.. _`oa_put_render_ctx_id.description`:

Description
-----------

In case anything needed doing to ensure the context HW ID would remain valid
for the lifetime of the stream, then that can be undone here.

.. _`i915_oa_stream_enable`:

i915_oa_stream_enable
=====================

.. c:function:: void i915_oa_stream_enable(struct i915_perf_stream *stream)

    handle `I915_PERF_IOCTL_ENABLE` for OA stream

    :param stream:
        An i915 perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

.. _`i915_oa_stream_enable.description`:

Description
-----------

[Re]enables hardware periodic sampling according to the period configured
when opening the stream. This also starts a hrtimer that will periodically
check for data in the circular OA buffer for notifying userspace (e.g.
during a \ :c:func:`read`\  or \ :c:func:`poll`\ ).

.. _`i915_oa_stream_disable`:

i915_oa_stream_disable
======================

.. c:function:: void i915_oa_stream_disable(struct i915_perf_stream *stream)

    handle `I915_PERF_IOCTL_DISABLE` for OA stream

    :param stream:
        An i915 perf stream opened for OA metrics
    :type stream: struct i915_perf_stream \*

.. _`i915_oa_stream_disable.description`:

Description
-----------

Stops the OA unit from periodically writing counter reports into the
circular OA buffer. This also stops the hrtimer that periodically checks for
data in the circular OA buffer, for notifying userspace.

.. _`i915_oa_stream_init`:

i915_oa_stream_init
===================

.. c:function:: int i915_oa_stream_init(struct i915_perf_stream *stream, struct drm_i915_perf_open_param *param, struct perf_open_properties *props)

    validate combined props for OA stream and init

    :param stream:
        An i915 perf stream
    :type stream: struct i915_perf_stream \*

    :param param:
        The open parameters passed to `DRM_I915_PERF_OPEN`
    :type param: struct drm_i915_perf_open_param \*

    :param props:
        The property state that configures stream (individually validated)
    :type props: struct perf_open_properties \*

.. _`i915_oa_stream_init.description`:

Description
-----------

While \ :c:func:`read_properties_unlocked`\  validates properties in isolation it
doesn't ensure that the combination necessarily makes sense.

At this point it has been determined that userspace wants a stream of
OA metrics, but still we need to further validate the combined
properties are OK.

If the configuration makes sense then we can allocate memory for
a circular OA buffer and apply the requested metric set configuration.

.. _`i915_oa_stream_init.return`:

Return
------

zero on success or a negative error code.

.. _`i915_perf_read_locked`:

i915_perf_read_locked
=====================

.. c:function:: ssize_t i915_perf_read_locked(struct i915_perf_stream *stream, struct file *file, char __user *buf, size_t count, loff_t *ppos)

    \ :c:type:`i915_perf_stream_ops->read <i915_perf_stream_ops>`\  with error normalisation

    :param stream:
        An i915 perf stream
    :type stream: struct i915_perf_stream \*

    :param file:
        An i915 perf stream file
    :type file: struct file \*

    :param buf:
        destination buffer given by userspace
    :type buf: char __user \*

    :param count:
        the number of bytes userspace wants to read
    :type count: size_t

    :param ppos:
        (inout) file seek position (unused)
    :type ppos: loff_t \*

.. _`i915_perf_read_locked.description`:

Description
-----------

Besides wrapping \ :c:type:`i915_perf_stream_ops->read <i915_perf_stream_ops>`\  this provides a common place to
ensure that if we've successfully copied any data then reporting that takes
precedence over any internal error status, so the data isn't lost.

For example ret will be -ENOSPC whenever there is more buffered data than
can be copied to userspace, but that's only interesting if we weren't able
to copy some data because it implies the userspace buffer is too small to
receive a single record (and we never split records).

Another case with ret == -EFAULT is more of a grey area since it would seem
like bad form for userspace to ask us to overrun its buffer, but the user

.. _`i915_perf_read_locked.knows-best`:

knows best
----------


  http://yarchive.net/comp/linux/partial_reads_writes.html

.. _`i915_perf_read_locked.return`:

Return
------

The number of bytes copied or a negative error code on failure.

.. _`i915_perf_read`:

i915_perf_read
==============

.. c:function:: ssize_t i915_perf_read(struct file *file, char __user *buf, size_t count, loff_t *ppos)

    handles \ :c:func:`read`\  FOP for i915 perf stream FDs

    :param file:
        An i915 perf stream file
    :type file: struct file \*

    :param buf:
        destination buffer given by userspace
    :type buf: char __user \*

    :param count:
        the number of bytes userspace wants to read
    :type count: size_t

    :param ppos:
        (inout) file seek position (unused)
    :type ppos: loff_t \*

.. _`i915_perf_read.description`:

Description
-----------

The entry point for handling a \ :c:func:`read`\  on a stream file descriptor from
userspace. Most of the work is left to the \ :c:func:`i915_perf_read_locked`\  and
\ :c:type:`i915_perf_stream_ops->read <i915_perf_stream_ops>`\  but to save having stream implementations (of
which we might have multiple later) we handle blocking read here.

We can also consistently treat trying to read from a disabled stream
as an IO error so implementations can assume the stream is enabled
while reading.

.. _`i915_perf_read.return`:

Return
------

The number of bytes copied or a negative error code on failure.

.. _`i915_perf_poll_locked`:

i915_perf_poll_locked
=====================

.. c:function:: __poll_t i915_perf_poll_locked(struct drm_i915_private *dev_priv, struct i915_perf_stream *stream, struct file *file, poll_table *wait)

    \ :c:func:`poll_wait`\  with a suitable wait queue for stream

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param stream:
        An i915 perf stream
    :type stream: struct i915_perf_stream \*

    :param file:
        An i915 perf stream file
    :type file: struct file \*

    :param wait:
        \ :c:func:`poll`\  state table
    :type wait: poll_table \*

.. _`i915_perf_poll_locked.description`:

Description
-----------

For handling userspace polling on an i915 perf stream, this calls through to
\ :c:type:`i915_perf_stream_ops->poll_wait <i915_perf_stream_ops>`\  to call \ :c:func:`poll_wait`\  with a wait queue that
will be woken for new stream data.

.. _`i915_perf_poll_locked.note`:

Note
----

The \ :c:type:`drm_i915_private->perf <drm_i915_private>`\ .lock mutex has been taken to serialize
with any non-file-operation driver hooks.

.. _`i915_perf_poll_locked.return`:

Return
------

any poll events that are ready without sleeping

.. _`i915_perf_poll`:

i915_perf_poll
==============

.. c:function:: __poll_t i915_perf_poll(struct file *file, poll_table *wait)

    call \ :c:func:`poll_wait`\  with a suitable wait queue for stream

    :param file:
        An i915 perf stream file
    :type file: struct file \*

    :param wait:
        \ :c:func:`poll`\  state table
    :type wait: poll_table \*

.. _`i915_perf_poll.description`:

Description
-----------

For handling userspace polling on an i915 perf stream, this ensures
\ :c:func:`poll_wait`\  gets called with a wait queue that will be woken for new stream
data.

.. _`i915_perf_poll.note`:

Note
----

Implementation deferred to \ :c:func:`i915_perf_poll_locked`\ 

.. _`i915_perf_poll.return`:

Return
------

any poll events that are ready without sleeping

.. _`i915_perf_enable_locked`:

i915_perf_enable_locked
=======================

.. c:function:: void i915_perf_enable_locked(struct i915_perf_stream *stream)

    handle `I915_PERF_IOCTL_ENABLE` ioctl

    :param stream:
        A disabled i915 perf stream
    :type stream: struct i915_perf_stream \*

.. _`i915_perf_enable_locked.description`:

Description
-----------

[Re]enables the associated capture of data for this stream.

If a stream was previously enabled then there's currently no intention
to provide userspace any guarantee about the preservation of previously
buffered data.

.. _`i915_perf_disable_locked`:

i915_perf_disable_locked
========================

.. c:function:: void i915_perf_disable_locked(struct i915_perf_stream *stream)

    handle `I915_PERF_IOCTL_DISABLE` ioctl

    :param stream:
        An enabled i915 perf stream
    :type stream: struct i915_perf_stream \*

.. _`i915_perf_disable_locked.description`:

Description
-----------

Disables the associated capture of data for this stream.

The intention is that disabling an re-enabling a stream will ideally be
cheaper than destroying and re-opening a stream with the same configuration,
though there are no formal guarantees about what state or buffered data
must be retained between disabling and re-enabling a stream.

.. _`i915_perf_disable_locked.note`:

Note
----

while a stream is disabled it's considered an error for userspace
to attempt to read from the stream (-EIO).

.. _`i915_perf_ioctl_locked`:

i915_perf_ioctl_locked
======================

.. c:function:: long i915_perf_ioctl_locked(struct i915_perf_stream *stream, unsigned int cmd, unsigned long arg)

    support \ :c:func:`ioctl`\  usage with i915 perf stream FDs

    :param stream:
        An i915 perf stream
    :type stream: struct i915_perf_stream \*

    :param cmd:
        the ioctl request
    :type cmd: unsigned int

    :param arg:
        the ioctl data
    :type arg: unsigned long

.. _`i915_perf_ioctl_locked.note`:

Note
----

The \ :c:type:`drm_i915_private->perf <drm_i915_private>`\ .lock mutex has been taken to serialize
with any non-file-operation driver hooks.

.. _`i915_perf_ioctl_locked.return`:

Return
------

zero on success or a negative error code. Returns -EINVAL for
an unknown ioctl request.

.. _`i915_perf_ioctl`:

i915_perf_ioctl
===============

.. c:function:: long i915_perf_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    support \ :c:func:`ioctl`\  usage with i915 perf stream FDs

    :param file:
        An i915 perf stream file
    :type file: struct file \*

    :param cmd:
        the ioctl request
    :type cmd: unsigned int

    :param arg:
        the ioctl data
    :type arg: unsigned long

.. _`i915_perf_ioctl.description`:

Description
-----------

Implementation deferred to \ :c:func:`i915_perf_ioctl_locked`\ .

.. _`i915_perf_ioctl.return`:

Return
------

zero on success or a negative error code. Returns -EINVAL for
an unknown ioctl request.

.. _`i915_perf_destroy_locked`:

i915_perf_destroy_locked
========================

.. c:function:: void i915_perf_destroy_locked(struct i915_perf_stream *stream)

    destroy an i915 perf stream

    :param stream:
        An i915 perf stream
    :type stream: struct i915_perf_stream \*

.. _`i915_perf_destroy_locked.description`:

Description
-----------

Frees all resources associated with the given i915 perf \ ``stream``\ , disabling
any associated data capture in the process.

.. _`i915_perf_destroy_locked.note`:

Note
----

The \ :c:type:`drm_i915_private->perf <drm_i915_private>`\ .lock mutex has been taken to serialize
with any non-file-operation driver hooks.

.. _`i915_perf_release`:

i915_perf_release
=================

.. c:function:: int i915_perf_release(struct inode *inode, struct file *file)

    handles userspace \ :c:func:`close`\  of a stream file

    :param inode:
        anonymous inode associated with file
    :type inode: struct inode \*

    :param file:
        An i915 perf stream file
    :type file: struct file \*

.. _`i915_perf_release.description`:

Description
-----------

Cleans up any resources associated with an open i915 perf stream file.

NB: \ :c:func:`close`\  can't really fail from the userspace point of view.

.. _`i915_perf_release.return`:

Return
------

zero on success or a negative error code.

.. _`i915_perf_open_ioctl_locked`:

i915_perf_open_ioctl_locked
===========================

.. c:function:: int i915_perf_open_ioctl_locked(struct drm_i915_private *dev_priv, struct drm_i915_perf_open_param *param, struct perf_open_properties *props, struct drm_file *file)

    DRM \ :c:func:`ioctl`\  for userspace to open a stream FD

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param param:
        The open parameters passed to 'DRM_I915_PERF_OPEN`
    :type param: struct drm_i915_perf_open_param \*

    :param props:
        individually validated u64 property value pairs
    :type props: struct perf_open_properties \*

    :param file:
        drm file
    :type file: struct drm_file \*

.. _`i915_perf_open_ioctl_locked.description`:

Description
-----------

See \ :c:func:`i915_perf_ioctl_open`\  for interface details.

Implements further stream config validation and stream initialization on
behalf of \ :c:func:`i915_perf_open_ioctl`\  with the \ :c:type:`drm_i915_private->perf <drm_i915_private>`\ .lock mutex
taken to serialize with any non-file-operation driver hooks.

.. _`i915_perf_open_ioctl_locked.note`:

Note
----

at this point the \ ``props``\  have only been validated in isolation and
it's still necessary to validate that the combination of properties makes
sense.

In the case where userspace is interested in OA unit metrics then further
config validation and stream initialization details will be handled by
\ :c:func:`i915_oa_stream_init`\ . The code here should only validate config state that
will be relevant to all stream types / backends.

.. _`i915_perf_open_ioctl_locked.return`:

Return
------

zero on success or a negative error code.

.. _`read_properties_unlocked`:

read_properties_unlocked
========================

.. c:function:: int read_properties_unlocked(struct drm_i915_private *dev_priv, u64 __user *uprops, u32 n_props, struct perf_open_properties *props)

    validate + copy userspace stream open properties

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param uprops:
        The array of u64 key value pairs given by userspace
    :type uprops: u64 __user \*

    :param n_props:
        The number of key value pairs expected in \ ``uprops``\ 
    :type n_props: u32

    :param props:
        The stream configuration built up while validating properties
    :type props: struct perf_open_properties \*

.. _`read_properties_unlocked.description`:

Description
-----------

Note this function only validates properties in isolation it doesn't
validate that the combination of properties makes sense or that all
properties necessary for a particular kind of stream have been set.

Note that there currently aren't any ordering requirements for properties so
we shouldn't validate or assume anything about ordering here. This doesn't
rule out defining new properties with ordering requirements in the future.

.. _`i915_perf_open_ioctl`:

i915_perf_open_ioctl
====================

.. c:function:: int i915_perf_open_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    DRM \ :c:func:`ioctl`\  for userspace to open a stream FD

    :param dev:
        drm device
    :type dev: struct drm_device \*

    :param data:
        ioctl data copied from userspace (unvalidated)
    :type data: void \*

    :param file:
        drm file
    :type file: struct drm_file \*

.. _`i915_perf_open_ioctl.description`:

Description
-----------

Validates the stream open parameters given by userspace including flags
and an array of u64 key, value pair properties.

Very little is assumed up front about the nature of the stream being
opened (for instance we don't assume it's for periodic OA unit metrics). An
i915-perf stream is expected to be a suitable interface for other forms of
buffered data written by the GPU besides periodic OA metrics.

Note we copy the properties from userspace outside of the i915 perf
mutex to avoid an awkward lockdep with mmap_sem.

Most of the implementation details are handled by
\ :c:func:`i915_perf_open_ioctl_locked`\  after taking the \ :c:type:`drm_i915_private->perf <drm_i915_private>`\ .lock
mutex for serializing with any non-file-operation driver hooks.

.. _`i915_perf_open_ioctl.return`:

Return
------

A newly opened i915 Perf stream file descriptor or negative
error code on failure.

.. _`i915_perf_register`:

i915_perf_register
==================

.. c:function:: void i915_perf_register(struct drm_i915_private *dev_priv)

    exposes i915-perf to userspace

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`i915_perf_register.description`:

Description
-----------

In particular OA metric sets are advertised under a sysfs metrics/
directory allowing userspace to enumerate valid IDs that can be
used to open an i915-perf stream.

.. _`i915_perf_unregister`:

i915_perf_unregister
====================

.. c:function:: void i915_perf_unregister(struct drm_i915_private *dev_priv)

    hide i915-perf from userspace

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`i915_perf_unregister.description`:

Description
-----------

i915-perf state cleanup is split up into an 'unregister' and
'deinit' phase where the interface is first hidden from
userspace by \ :c:func:`i915_perf_unregister`\  before cleaning up
remaining state in \ :c:func:`i915_perf_fini`\ .

.. _`i915_perf_add_config_ioctl`:

i915_perf_add_config_ioctl
==========================

.. c:function:: int i915_perf_add_config_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    DRM \ :c:func:`ioctl`\  for userspace to add a new OA config

    :param dev:
        drm device
    :type dev: struct drm_device \*

    :param data:
        ioctl data (pointer to struct drm_i915_perf_oa_config) copied from
        userspace (unvalidated)
    :type data: void \*

    :param file:
        drm file
    :type file: struct drm_file \*

.. _`i915_perf_add_config_ioctl.description`:

Description
-----------

Validates the submitted OA register to be saved into a new OA config that
can then be used for programming the OA unit and its NOA network.

.. _`i915_perf_add_config_ioctl.return`:

Return
------

A new allocated config number to be used with the perf open ioctl
or a negative error code on failure.

.. _`i915_perf_remove_config_ioctl`:

i915_perf_remove_config_ioctl
=============================

.. c:function:: int i915_perf_remove_config_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    DRM \ :c:func:`ioctl`\  for userspace to remove an OA config

    :param dev:
        drm device
    :type dev: struct drm_device \*

    :param data:
        ioctl data (pointer to u64 integer) copied from userspace
    :type data: void \*

    :param file:
        drm file
    :type file: struct drm_file \*

.. _`i915_perf_remove_config_ioctl.description`:

Description
-----------

Configs can be removed while being used, the will stop appearing in sysfs
and their content will be freed when the stream using the config is closed.

.. _`i915_perf_remove_config_ioctl.return`:

Return
------

0 on success or a negative error code on failure.

.. _`i915_perf_init`:

i915_perf_init
==============

.. c:function:: void i915_perf_init(struct drm_i915_private *dev_priv)

    initialize i915-perf state on module load

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`i915_perf_init.description`:

Description
-----------

Initializes i915-perf state without exposing anything to userspace.

.. _`i915_perf_init.note`:

Note
----

i915-perf initialization is split into an 'init' and 'register'
phase with the \ :c:func:`i915_perf_register`\  exposing state to userspace.

.. _`i915_perf_fini`:

i915_perf_fini
==============

.. c:function:: void i915_perf_fini(struct drm_i915_private *dev_priv)

    Counter part to \ :c:func:`i915_perf_init`\ 

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. This file was automatic generated / don't edit.

