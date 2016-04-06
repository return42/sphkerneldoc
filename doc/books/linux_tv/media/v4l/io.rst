
.. _io:

============
Input/Output
============

The V4L2 API defines several different methods to read from or write to a device. All drivers exchanging data with applications must support at least one of them.

The classic I/O method using the ``read()`` and ``write()`` function is automatically selected after opening a V4L2 device. When the driver does not support this method attempts to
read or write will fail at any time.

Other methods must be negotiated. To select the streaming I/O method with memory mapped or user buffers applications call the :ref:`VIDIOC_REQBUFS <vidioc-reqbufs>` ioctl. The
asynchronous I/O method is not defined yet.

Video overlay can be considered another I/O method, although the application does not directly receive the image data. It is selected by initiating video overlay with the
:ref:`VIDIOC_S_FMT <vidioc-g-fmt>` ioctl. For more information see :ref:`overlay`.

Generally exactly one I/O method, including overlay, is associated with each file descriptor. The only exceptions are applications not exchanging data with a driver ("panel
applications", see :ref:`open`) and drivers permitting simultaneous video capturing and overlay using the same file descriptor, for compatibility with V4L and earlier versions of
V4L2.

``VIDIOC_S_FMT`` and ``VIDIOC_REQBUFS`` would permit this to some degree, but for simplicity drivers need not support switching the I/O method (after first switching away from
read/write) other than by closing and reopening the device.

The following sections describe the various I/O methods in more detail.


.. _rw:

Read/Write
==========

Input and output devices support the ``read()`` and ``write()`` function, respectively, when the ``V4L2_CAP_READWRITE`` flag in the ``capabilities`` field of struct
:ref:`v4l2_capability <v4l2-capability>` returned by the :ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl is set.

Drivers may need the CPU to copy the data, but they may also support DMA to or from user memory, so this I/O method is not necessarily less efficient than other methods merely
exchanging buffer pointers. It is considered inferior though because no meta-information like frame counters or timestamps are passed. This information is necessary to recognize
frame dropping and to synchronize with other data streams. However this is also the simplest I/O method, requiring little or no setup to exchange data. It permits command line
stunts like this (the vidctrl tool is fictitious):



::

    > vidctrl /dev/video --input=0 --format=YUYV --size=352x288
    > dd if=/dev/video of=myimage.422 bs=202752 count=1
To read from the device applications use the :ref:`read() <func-read>` function, to write the :ref:`write() <func-write>` function. Drivers must implement one I/O method if
they exchange data with applications, but it need not be this. [1]_ When reading or writing is supported, the driver must also support the :ref:`select() <func-select>` and
:ref:`poll() <func-poll>` function. [2]_


.. _mmap:

Streaming I/O (Memory Mapping)
==============================

Input and output devices support this I/O method when the ``V4L2_CAP_STREAMING`` flag in the ``capabilities`` field of struct :ref:`v4l2_capability <v4l2-capability>` returned
by the :ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl is set. There are two streaming methods, to determine if the memory mapping flavor is supported applications must call the
:ref:`VIDIOC_REQBUFS <vidioc-reqbufs>` ioctl.

Streaming is an I/O method where only pointers to buffers are exchanged between application and driver, the data itself is not copied. Memory mapping is primarily intended to map
buffers in device memory into the application's address space. Device memory can be for example the video memory on a graphics card with a video capture add-on. However, being the
most efficient I/O method available for a long time, many other drivers support streaming as well, allocating buffers in DMA-able main memory.

A driver can support many sets of buffers. Each set is identified by a unique buffer type value. The sets are independent and each set can hold a different type of data. To access
different sets at the same time different file descriptors must be used. [3]_

To allocate device buffers applications call the :ref:`VIDIOC_REQBUFS <vidioc-reqbufs>` ioctl with the desired number of buffers and buffer type, for example
``V4L2_BUF_TYPE_VIDEO_CAPTURE``. This ioctl can also be used to change the number of buffers or to free the allocated memory, provided none of the buffers are still mapped.

Before applications can access the buffers they must map them into their address space with the :ref:`mmap() <func-mmap>` function. The location of the buffers in device memory
can be determined with the :ref:`VIDIOC_QUERYBUF <vidioc-querybuf>` ioctl. In the single-planar API case, the ``m.offset`` and ``length`` returned in a struct
:ref:`v4l2_buffer <v4l2-buffer>` are passed as sixth and second parameter to the ``mmap()`` function. When using the multi-planar API, struct :ref:`v4l2_buffer <v4l2-buffer>`
contains an array of struct :ref:`v4l2_plane <v4l2-plane>` structures, each containing its own ``m.offset`` and ``length``. When using the multi-planar API, every plane of every
buffer has to be mapped separately, so the number of calls to :ref:`mmap() <func-mmap>` should be equal to number of buffers times number of planes in each buffer. The offset and
length values must not be modified. Remember, the buffers are allocated in physical memory, as opposed to virtual memory, which can be swapped out to disk. Applications should free
the buffers as soon as possible with the :ref:`munmap() <func-munmap>` function.


.. code-block:: c

    struct v4l2_requestbuffers reqbuf;
    struct {
        void *start;
        size_t length;
    } *buffers;
    unsigned int i;

    memset(&reqbuf, 0, sizeof(reqbuf));
    reqbuf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    reqbuf.memory = V4L2_MEMORY_MMAP;
    reqbuf.count = 20;

    if (-1 == ioctl (fd, VIDIOC_REQBUFS, &reqbuf)) {
        if (errno == EINVAL)
            printf("Video capturing or mmap-streaming is not supported\\n");
        else
            perror("VIDIOC_REQBUFS");

        exit(EXIT_FAILURE);
    }

    /* We want at least five buffers. */

    if (reqbuf.count < 5) {
        /* You may need to free the buffers here. */
        printf("Not enough buffer memory\\n");
        exit(EXIT_FAILURE);
    }

    buffers = calloc(reqbuf.count, sizeof(*buffers));
    assert(buffers != NULL);

    for (i = 0; i < reqbuf.count; i++) {
        struct v4l2_buffer buffer;

        memset(&buffer, 0, sizeof(buffer));
        buffer.type = reqbuf.type;
        buffer.memory = V4L2_MEMORY_MMAP;
        buffer.index = i;

        if (-1 == ioctl (fd, VIDIOC_QUERYBUF, &buffer)) {
            perror("VIDIOC_QUERYBUF");
            exit(EXIT_FAILURE);
        }

        buffers[i].length = buffer.length; /* remember for munmap() */

        buffers[i].start = mmap(NULL, buffer.length,
                    PROT_READ | PROT_WRITE, /* recommended */
                    MAP_SHARED,             /* recommended */
                    fd, buffer.m.offset);

        if (MAP_FAILED == buffers[i].start) {
            /* If you do not exit here you should unmap() and free()
               the buffers mapped so far. */
            perror("mmap");
            exit(EXIT_FAILURE);
        }
    }

    /* Cleanup. */

    for (i = 0; i < reqbuf.count; i++)
        munmap(buffers[i].start, buffers[i].length);


.. code-block:: c

    struct v4l2_requestbuffers reqbuf;
    /* Our current format uses 3 planes per buffer */
    #define FMT_NUM_PLANES = 3

    struct {
        void *start[FMT_NUM_PLANES];
        size_t length[FMT_NUM_PLANES];
    } *buffers;
    unsigned int i, j;

    memset(&reqbuf, 0, sizeof(reqbuf));
    reqbuf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE;
    reqbuf.memory = V4L2_MEMORY_MMAP;
    reqbuf.count = 20;

    if (ioctl(fd, VIDIOC_REQBUFS, &reqbuf) < 0) {
        if (errno == EINVAL)
            printf("Video capturing or mmap-streaming is not supported\\n");
        else
            perror("VIDIOC_REQBUFS");

        exit(EXIT_FAILURE);
    }

    /* We want at least five buffers. */

    if (reqbuf.count < 5) {
        /* You may need to free the buffers here. */
        printf("Not enough buffer memory\\n");
        exit(EXIT_FAILURE);
    }

    buffers = calloc(reqbuf.count, sizeof(*buffers));
    assert(buffers != NULL);

    for (i = 0; i < reqbuf.count; i++) {
        struct v4l2_buffer buffer;
        struct v4l2_plane planes[FMT_NUM_PLANES];

        memset(&buffer, 0, sizeof(buffer));
        buffer.type = reqbuf.type;
        buffer.memory = V4L2_MEMORY_MMAP;
        buffer.index = i;
        /* length in struct v4l2_buffer in multi-planar API stores the size
         * of planes array. */
        buffer.length = FMT_NUM_PLANES;
        buffer.m.planes = planes;

        if (ioctl(fd, VIDIOC_QUERYBUF, &buffer) < 0) {
            perror("VIDIOC_QUERYBUF");
            exit(EXIT_FAILURE);
        }

        /* Every plane has to be mapped separately */
        for (j = 0; j < FMT_NUM_PLANES; j++) {
            buffers[i].length[j] = buffer.m.planes[j].length; /* remember for munmap() */

            buffers[i].start[j] = mmap(NULL, buffer.m.planes[j].length,
                     PROT_READ | PROT_WRITE, /* recommended */
                     MAP_SHARED,             /* recommended */
                     fd, buffer.m.planes[j].m.offset);

            if (MAP_FAILED == buffers[i].start[j]) {
                /* If you do not exit here you should unmap() and free()
                   the buffers and planes mapped so far. */
                perror("mmap");
                exit(EXIT_FAILURE);
            }
        }
    }

    /* Cleanup. */

    for (i = 0; i < reqbuf.count; i++)
        for (j = 0; j < FMT_NUM_PLANES; j++)
            munmap(buffers[i].start[j], buffers[i].length[j]);

Conceptually streaming drivers maintain two buffer queues, an incoming and an outgoing queue. They separate the synchronous capture or output operation locked to a video clock from
the application which is subject to random disk or network delays and preemption by other processes, thereby reducing the probability of data loss. The queues are organized as
FIFOs, buffers will be output in the order enqueued in the incoming FIFO, and were captured in the order dequeued from the outgoing FIFO.

The driver may require a minimum number of buffers enqueued at all times to function, apart of this no limit exists on the number of buffers applications can enqueue in advance, or
dequeue and process. They can also enqueue in a different order than buffers have been dequeued, and the driver can *fill* enqueued *empty* buffers in any order.  [4]_ The index
number of a buffer (struct :ref:`v4l2_buffer <v4l2-buffer>` ``index``) plays no role here, it only identifies the buffer.

Initially all mapped buffers are in dequeued state, inaccessible by the driver. For capturing applications it is customary to first enqueue all mapped buffers, then to start
capturing and enter the read loop. Here the application waits until a filled buffer can be dequeued, and re-enqueues the buffer when the data is no longer needed. Output
applications fill and enqueue buffers, when enough buffers are stacked up the output is started with ``VIDIOC_STREAMON``. In the write loop, when the application runs out of free
buffers, it must wait until an empty buffer can be dequeued and reused.

To enqueue and dequeue a buffer applications use the :ref:`VIDIOC_QBUF <vidioc-qbuf>` and :ref:`VIDIOC_DQBUF <vidioc-qbuf>` ioctl. The status of a buffer being mapped,
enqueued, full or empty can be determined at any time using the :ref:`VIDIOC_QUERYBUF <vidioc-querybuf>` ioctl. Two methods exist to suspend execution of the application until
one or more buffers can be dequeued. By default ``VIDIOC_DQBUF`` blocks when no buffer is in the outgoing queue. When the ``O_NONBLOCK`` flag was given to the
:ref:`open() <func-open>` function, ``VIDIOC_DQBUF`` returns immediately with an EAGAIN error code when no buffer is available. The :ref:`select() <func-select>` or
:ref:`poll() <func-poll>` functions are always available.

To start and stop capturing or output applications call the :ref:`VIDIOC_STREAMON <vidioc-streamon>` and :ref:`VIDIOC_STREAMOFF <vidioc-streamon>` ioctl. Note
``VIDIOC_STREAMOFF`` removes all buffers from both queues as a side effect. Since there is no notion of doing anything "now" on a multitasking system, if an application needs to
synchronize with another event it should examine the struct :ref:`v4l2_buffer <v4l2-buffer>` ``timestamp`` of captured or outputted buffers.

Drivers implementing memory mapping I/O must support the ``VIDIOC_REQBUFS``, ``VIDIOC_QUERYBUF``, ``VIDIOC_QBUF``, ``VIDIOC_DQBUF``, ``VIDIOC_STREAMON`` and ``VIDIOC_STREAMOFF``
ioctl, the ``mmap()``, ``munmap()``, ``select()`` and ``poll()`` function. [5]_

[capture example]


.. _userp:

Streaming I/O (User Pointers)
=============================

Input and output devices support this I/O method when the ``V4L2_CAP_STREAMING`` flag in the ``capabilities`` field of struct :ref:`v4l2_capability <v4l2-capability>` returned
by the :ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl is set. If the particular user pointer method (not only memory mapping) is supported must be determined by calling the
:ref:`VIDIOC_REQBUFS <vidioc-reqbufs>` ioctl.

This I/O method combines advantages of the read/write and memory mapping methods. Buffers (planes) are allocated by the application itself, and can reside for example in virtual or
shared memory. Only pointers to data are exchanged, these pointers and meta-information are passed in struct :ref:`v4l2_buffer <v4l2-buffer>` (or in struct
:ref:`v4l2_plane <v4l2-plane>` in the multi-planar API case). The driver must be switched into user pointer I/O mode by calling the :ref:`VIDIOC_REQBUFS <vidioc-reqbufs>`
with the desired buffer type. No buffers (planes) are allocated beforehand, consequently they are not indexed and cannot be queried like mapped buffers with the ``VIDIOC_QUERYBUF``
ioctl.


.. code-block:: c

    struct v4l2_requestbuffers reqbuf;

    memset (&reqbuf, 0, sizeof (reqbuf));
    reqbuf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    reqbuf.memory = V4L2_MEMORY_USERPTR;

    if (ioctl (fd, VIDIOC_REQBUFS, &reqbuf) == -1) {
        if (errno == EINVAL)
            printf ("Video capturing or user pointer streaming is not supported\\n");
        else
            perror ("VIDIOC_REQBUFS");

        exit (EXIT_FAILURE);
    }

Buffer (plane) addresses and sizes are passed on the fly with the :ref:`VIDIOC_QBUF <vidioc-qbuf>` ioctl. Although buffers are commonly cycled, applications can pass different
addresses and sizes at each ``VIDIOC_QBUF`` call. If required by the hardware the driver swaps memory pages within physical memory to create a continuous area of memory. This
happens transparently to the application in the virtual memory subsystem of the kernel. When buffer pages have been swapped out to disk they are brought back and finally locked in
physical memory for DMA. [6]_

Filled or displayed buffers are dequeued with the :ref:`VIDIOC_DQBUF <vidioc-qbuf>` ioctl. The driver can unlock the memory pages at any time between the completion of the DMA
and this ioctl. The memory is also unlocked when :ref:`VIDIOC_STREAMOFF <vidioc-streamon>` is called, :ref:`VIDIOC_REQBUFS <vidioc-reqbufs>`, or when the device is closed.
Applications must take care not to free buffers without dequeuing. For once, the buffers remain locked until further, wasting physical memory. Second the driver will not be
notified when the memory is returned to the application's free list and subsequently reused for other purposes, possibly completing the requested DMA and overwriting valuable data.

For capturing applications it is customary to enqueue a number of empty buffers, to start capturing and enter the read loop. Here the application waits until a filled buffer can be
dequeued, and re-enqueues the buffer when the data is no longer needed. Output applications fill and enqueue buffers, when enough buffers are stacked up output is started. In the
write loop, when the application runs out of free buffers it must wait until an empty buffer can be dequeued and reused. Two methods exist to suspend execution of the application
until one or more buffers can be dequeued. By default ``VIDIOC_DQBUF`` blocks when no buffer is in the outgoing queue. When the ``O_NONBLOCK`` flag was given to the
:ref:`open() <func-open>` function, ``VIDIOC_DQBUF`` returns immediately with an EAGAIN error code when no buffer is available. The :ref:`select() <func-select>` or
:ref:`poll() <func-poll>` function are always available.

To start and stop capturing or output applications call the :ref:`VIDIOC_STREAMON <vidioc-streamon>` and :ref:`VIDIOC_STREAMOFF <vidioc-streamon>` ioctl. Note
``VIDIOC_STREAMOFF`` removes all buffers from both queues and unlocks all buffers as a side effect. Since there is no notion of doing anything "now" on a multitasking system, if an
application needs to synchronize with another event it should examine the struct :ref:`v4l2_buffer <v4l2-buffer>` ``timestamp`` of captured or outputted buffers.

Drivers implementing user pointer I/O must support the ``VIDIOC_REQBUFS``, ``VIDIOC_QBUF``, ``VIDIOC_DQBUF``, ``VIDIOC_STREAMON`` and ``VIDIOC_STREAMOFF`` ioctl, the ``select()``
and ``poll()`` function. [7]_


.. _dmabuf:

Streaming I/O (DMA buffer importing)
====================================

    **Note**

    This is an :ref:`experimental <experimental>` interface and may change in the future.

The DMABUF framework provides a generic method for sharing buffers between multiple devices. Device drivers that support DMABUF can export a DMA buffer to userspace as a file
descriptor (known as the exporter role), import a DMA buffer from userspace using a file descriptor previously exported for a different or the same device (known as the importer
role), or both. This section describes the DMABUF importer role API in V4L2.

Refer to :ref:`DMABUF exporting <vidioc-expbuf>` for details about exporting V4L2 buffers as DMABUF file descriptors.

Input and output devices support the streaming I/O method when the ``V4L2_CAP_STREAMING`` flag in the ``capabilities`` field of struct :ref:`v4l2_capability <v4l2-capability>`
returned by the :ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl is set. Whether importing DMA buffers through DMABUF file descriptors is supported is determined by calling the
:ref:`VIDIOC_REQBUFS <vidioc-reqbufs>` ioctl with the memory type set to ``V4L2_MEMORY_DMABUF``.

This I/O method is dedicated to sharing DMA buffers between different devices, which may be V4L devices or other video-related devices (e.g. DRM). Buffers (planes) are allocated by
a driver on behalf of an application. Next, these buffers are exported to the application as file descriptors using an API which is specific for an allocator driver. Only such file
descriptor are exchanged. The descriptors and meta-information are passed in struct :ref:`v4l2_buffer <v4l2-buffer>` (or in struct :ref:`v4l2_plane <v4l2-plane>` in the
multi-planar API case). The driver must be switched into DMABUF I/O mode by calling the :ref:`VIDIOC_REQBUFS <vidioc-reqbufs>` with the desired buffer type.


.. code-block:: c

    struct v4l2_requestbuffers reqbuf;

    memset(&reqbuf, 0, sizeof (reqbuf));
    reqbuf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    reqbuf.memory = V4L2_MEMORY_DMABUF;
    reqbuf.count = 1;

    if (ioctl(fd, VIDIOC_REQBUFS, &reqbuf) == -1) {
        if (errno == EINVAL)
            printf("Video capturing or DMABUF streaming is not supported\\n");
        else
            perror("VIDIOC_REQBUFS");

        exit(EXIT_FAILURE);
    }

The buffer (plane) file descriptor is passed on the fly with the :ref:`VIDIOC_QBUF <vidioc-qbuf>` ioctl. In case of multiplanar buffers, every plane can be associated with a
different DMABUF descriptor. Although buffers are commonly cycled, applications can pass a different DMABUF descriptor at each ``VIDIOC_QBUF`` call.


.. code-block:: c

    int buffer_queue(int v4lfd, int index, int dmafd)
    {
        struct v4l2_buffer buf;

        memset(&buf, 0, sizeof buf);
        buf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
        buf.memory = V4L2_MEMORY_DMABUF;
        buf.index = index;
        buf.m.fd = dmafd;

        if (ioctl(v4lfd, VIDIOC_QBUF, &buf) == -1) {
            perror("VIDIOC_QBUF");
            return -1;
        }

        return 0;
    }


.. code-block:: c

    int buffer_queue_mp(int v4lfd, int index, int dmafd[], int n_planes)
    {
        struct v4l2_buffer buf;
        struct v4l2_plane planes[VIDEO_MAX_PLANES];
        int i;

        memset(&buf, 0, sizeof buf);
        buf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE;
        buf.memory = V4L2_MEMORY_DMABUF;
        buf.index = index;
        buf.m.planes = planes;
        buf.length = n_planes;

        memset(&planes, 0, sizeof planes);

        for (i = 0; i < n_planes; ++i)
            buf.m.planes[i].m.fd = dmafd[i];

        if (ioctl(v4lfd, VIDIOC_QBUF, &buf) == -1) {
            perror("VIDIOC_QBUF");
            return -1;
        }

        return 0;
    }

Captured or displayed buffers are dequeued with the :ref:`VIDIOC_DQBUF <vidioc-qbuf>` ioctl. The driver can unlock the buffer at any time between the completion of the DMA and
this ioctl. The memory is also unlocked when :ref:`VIDIOC_STREAMOFF <vidioc-streamon>` is called, :ref:`VIDIOC_REQBUFS <vidioc-reqbufs>`, or when the device is closed.

For capturing applications it is customary to enqueue a number of empty buffers, to start capturing and enter the read loop. Here the application waits until a filled buffer can be
dequeued, and re-enqueues the buffer when the data is no longer needed. Output applications fill and enqueue buffers, when enough buffers are stacked up output is started. In the
write loop, when the application runs out of free buffers it must wait until an empty buffer can be dequeued and reused. Two methods exist to suspend execution of the application
until one or more buffers can be dequeued. By default ``VIDIOC_DQBUF`` blocks when no buffer is in the outgoing queue. When the ``O_NONBLOCK`` flag was given to the
:ref:`open() <func-open>` function, ``VIDIOC_DQBUF`` returns immediately with an EAGAIN error code when no buffer is available. The :ref:`select() <func-select>` and
:ref:`poll() <func-poll>` functions are always available.

To start and stop capturing or displaying applications call the :ref:`VIDIOC_STREAMON <vidioc-streamon>` and :ref:`VIDIOC_STREAMOFF <vidioc-streamon>` ioctls. Note that
``VIDIOC_STREAMOFF`` removes all buffers from both queues and unlocks all buffers as a side effect. Since there is no notion of doing anything "now" on a multitasking system, if an
application needs to synchronize with another event it should examine the struct :ref:`v4l2_buffer <v4l2-buffer>` ``timestamp`` of captured or outputted buffers.

Drivers implementing DMABUF importing I/O must support the ``VIDIOC_REQBUFS``, ``VIDIOC_QBUF``, ``VIDIOC_DQBUF``, ``VIDIOC_STREAMON`` and ``VIDIOC_STREAMOFF`` ioctls, and the
``select()`` and ``poll()`` functions.


.. _async:

Asynchronous I/O
================

This method is not defined yet.


.. _buffer:

Buffers
=======

A buffer contains data exchanged by application and driver using one of the Streaming I/O methods. In the multi-planar API, the data is held in planes, while the buffer structure
acts as a container for the planes. Only pointers to buffers (planes) are exchanged, the data itself is not copied. These pointers, together with meta-information like timestamps
or field parity, are stored in a struct ``v4l2_buffer``, argument to the :ref:`VIDIOC_QUERYBUF <vidioc-querybuf>`, :ref:`VIDIOC_QBUF <vidioc-qbuf>` and
:ref:`VIDIOC_DQBUF <vidioc-qbuf>` ioctl. In the multi-planar API, some plane-specific members of struct ``v4l2_buffer``, such as pointers and sizes for each plane, are stored in
struct ``v4l2_plane`` instead. In that case, struct ``v4l2_buffer`` contains an array of plane structures.

Dequeued video buffers come with timestamps. The driver decides at which part of the frame and with which clock the timestamp is taken. Please see flags in the masks
``V4L2_BUF_FLAG_TIMESTAMP_MASK`` and ``V4L2_BUF_FLAG_TSTAMP_SRC_MASK`` in :ref:`buffer-flags`. These flags are always valid and constant across all buffers during the whole video
stream. Changes in these flags may take place as a side effect of :ref:`VIDIOC_S_INPUT <vidioc-g-input>` or :ref:`VIDIOC_S_OUTPUT <vidioc-g-output>` however. The
``V4L2_BUF_FLAG_TIMESTAMP_COPY`` timestamp type which is used by e.g. on mem-to-mem devices is an exception to the rule: the timestamp source flags are copied from the OUTPUT video
buffer to the CAPTURE video buffer.


.. _v4l2-buffer:

struct v4l2_buffer
==================

::

    TODO ... 


    <table frame="none" pgwide="1" id="v4l2-buffer">
          <title>struct <structname>v4l2_buffer</structname></title>
          <tgroup cols="4">
        <colspec colname="c1" colwidth="1*"/><colspec colname="c2" colwidth="1*"/><colspec colname="c3" colwidth="1*"/><colspec colname="c4" colwidth="2*"/><spanspec spanname="hspan" namest="c1" nameend="c4"/>
        <tbody valign="top">
          <row>
            <entry>__u32</entry>
            <entry><structfield>index</structfield></entry>
            <entry/>
            <entry>Number of the buffer, set by the application except
    when calling <link linkend="vidioc-qbuf"><constant>VIDIOC_DQBUF</constant></link>, then it is set by the driver.
    This field can range from zero to the number of buffers allocated
    with the <link linkend="vidioc-reqbufs"><constant>VIDIOC_REQBUFS</constant></link> ioctl (struct <link linkend="v4l2-requestbuffers">v4l2_requestbuffers</link> <structfield>count</structfield>),
    plus any buffers allocated with <link linkend="vidioc-create-bufs"><constant>VIDIOC_CREATE_BUFS</constant></link> minus one.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>type</structfield></entry>
            <entry/>
            <entry>Type of the buffer, same as struct <link linkend="v4l2-format">v4l2_format</link>
    <structfield>type</structfield> or struct <link linkend="v4l2-requestbuffers">v4l2_requestbuffers</link>
    <structfield>type</structfield>, set by the application. See <xref linkend="v4l2-buf-type"/></entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>bytesused</structfield></entry>
            <entry/>
            <entry>The number of bytes occupied by the data in the
    buffer. It depends on the negotiated data format and may change with
    each buffer for compressed variable size data like JPEG images.
    Drivers must set this field when <structfield>type</structfield>
    refers to a capture stream, applications when it refers to an output stream.
    If the application sets this to 0 for an output stream, then
    <structfield>bytesused</structfield> will be set to the size of the
    buffer (see the <structfield>length</structfield> field of this struct) by
    the driver. For multiplanar formats this field is ignored and the
    <structfield>planes</structfield> pointer is used instead.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>flags</structfield></entry>
            <entry/>
            <entry>Flags set by the application or driver, see <xref linkend="buffer-flags"/>.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>field</structfield></entry>
            <entry/>
            <entry>Indicates the field order of the image in the
    buffer, see <xref linkend="v4l2-field"/>. This field is not used when
    the buffer contains VBI data. Drivers must set it when
    <structfield>type</structfield> refers to a capture stream,
    applications when it refers to an output stream.</entry>
          </row>
          <row>
            <entry>struct timeval</entry>
            <entry><structfield>timestamp</structfield></entry>
            <entry/>
            <entry><para>For capture streams this is time when the first data
            byte was captured, as returned by the
            <function>clock_gettime()</function> function for the relevant
            clock id; see <constant>V4L2_BUF_FLAG_TIMESTAMP_⋆</constant> in
            <xref linkend="buffer-flags"/>. For output streams the driver
            stores the time at which the last data byte was actually sent out
            in the  <structfield>timestamp</structfield> field. This permits
            applications to monitor the drift between the video and system
            clock. For output streams that use <constant>V4L2_BUF_FLAG_TIMESTAMP_COPY</constant>
            the application has to fill in the timestamp which will be copied
            by the driver to the capture stream.</para></entry>
          </row>
          <row>
            <entry>struct <link linkend="v4l2-timecode">v4l2_timecode</link></entry>
            <entry><structfield>timecode</structfield></entry>
            <entry/>
            <entry>When <structfield>type</structfield> is
    <constant>V4L2_BUF_TYPE_VIDEO_CAPTURE</constant> and the
    <constant>V4L2_BUF_FLAG_TIMECODE</constant> flag is set in
    <structfield>flags</structfield>, this structure contains a frame
    timecode. In <link linkend="v4l2-field">V4L2_FIELD_ALTERNATE</link>
    mode the top and bottom field contain the same timecode.
    Timecodes are intended to help video editing and are typically recorded on
    video tapes, but also embedded in compressed formats like MPEG. This
    field is independent of the <structfield>timestamp</structfield> and
    <structfield>sequence</structfield> fields.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>sequence</structfield></entry>
            <entry/>
            <entry>Set by the driver, counting the frames (not fields!) in
    sequence. This field is set for both input and output devices.</entry>
          </row>
          <row>
            <entry spanname="hspan"><para>In <link linkend="v4l2-field">V4L2_FIELD_ALTERNATE</link> mode the top and
    bottom field have the same sequence number. The count starts at zero
    and includes dropped or repeated frames. A dropped frame was received
    by an input device but could not be stored due to lack of free buffer
    space. A repeated frame was displayed again by an output device
    because the application did not pass new data in
    time.</para><para>Note this may count the frames received
    e.g. over USB, without taking into account the frames dropped by the
    remote hardware due to limited compression throughput or bus
    bandwidth. These devices identify by not enumerating any video
    standards, see <xref linkend="standard"/>.</para></entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>memory</structfield></entry>
            <entry/>
            <entry>This field must be set by applications and/or drivers
    in accordance with the selected I/O method. See <xref linkend="v4l2-memory"/></entry>
          </row>
          <row>
            <entry>union</entry>
            <entry><structfield>m</structfield></entry>
          </row>
          <row>
            <entry/>
            <entry>__u32</entry>
            <entry><structfield>offset</structfield></entry>
            <entry>For the single-planar API and when
    <structfield>memory</structfield> is <constant>V4L2_MEMORY_MMAP</constant> this
    is the offset of the buffer from the start of the device memory. The value is
    returned by the driver and apart of serving as parameter to the <link linkend="func-mmap"><function>mmap()</function></link>
    function not useful for applications. See <xref linkend="mmap"/> for details
          </entry>
          </row>
          <row>
            <entry/>
            <entry>unsigned long</entry>
            <entry><structfield>userptr</structfield></entry>
            <entry>For the single-planar API and when
    <structfield>memory</structfield> is <constant>V4L2_MEMORY_USERPTR</constant>
    this is a pointer to the buffer (casted to unsigned long type) in virtual
    memory, set by the application. See <xref linkend="userp"/> for details.
            </entry>
          </row>
          <row>
            <entry/>
            <entry>struct v4l2_plane</entry>
            <entry><structfield>⋆planes</structfield></entry>
            <entry>When using the multi-planar API, contains a userspace pointer
            to an array of struct <link linkend="v4l2-plane">v4l2_plane</link>. The size of the array should be put
            in the <structfield>length</structfield> field of this
            <structname>v4l2_buffer</structname> structure.</entry>
          </row>
          <row>
            <entry/>
            <entry>int</entry>
            <entry><structfield>fd</structfield></entry>
            <entry>For the single-plane API and when
    <structfield>memory</structfield> is <constant>V4L2_MEMORY_DMABUF</constant> this
    is the file descriptor associated with a DMABUF buffer.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>length</structfield></entry>
            <entry/>
            <entry>Size of the buffer (not the payload) in bytes for the
            single-planar API. This is set by the driver based on the calls to
            <link linkend="vidioc-reqbufs"><constant>VIDIOC_REQBUFS</constant></link> and/or <link linkend="vidioc-create-bufs"><constant>VIDIOC_CREATE_BUFS</constant></link>. For the multi-planar API the application sets
            this to the number of elements in the <structfield>planes</structfield>
            array. The driver will fill in the actual number of valid elements in
            that array.
            </entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>reserved2</structfield></entry>
            <entry/>
            <entry>A place holder for future extensions. Drivers and applications
    must set this to 0.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>reserved</structfield></entry>
            <entry/>
            <entry>A place holder for future extensions. Drivers and applications
    must set this to 0.</entry>
          </row>
        </tbody>
          </tgroup>
        </table>




.. _v4l2-plane:

.. table:: struct v4l2_plane

    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------------------------------------------+
    | __u32                                | ``bytesused``                        |                                      | The number of bytes occupied by data in the plane (its payload). Drivers |
    |                                      |                                      |                                      | must set this field when ``type`` refers to a capture stream,            |
    |                                      |                                      |                                      | applications when it refers to an output stream. If the application sets |
    |                                      |                                      |                                      | this to 0 for an output stream, then ``bytesused`` will be set to the    |
    |                                      |                                      |                                      | size of the plane (see the ``length`` field of this struct) by the       |
    |                                      |                                      |                                      | driver. Note that the actual image data starts at ``data_offset`` which  |
    |                                      |                                      |                                      | may not be 0.                                                            |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------------------------------------------+
    | __u32                                | ``length``                           |                                      | Size in bytes of the plane (not its payload). This is set by the driver  |
    |                                      |                                      |                                      | based on the calls to :ref:`VIDIOC_REQBUFS   <vidioc-reqbufs>`  and/or   |
    |                                      |                                      |                                      | :ref:`VIDIOC_CREATE_BUFS    <vidioc-create-bufs>`.                       |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------------------------------------------+
    | union                                | ``m``                                |                                      |                                                                          |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------------------------------------------+
    |                                      | __u32                                | ``mem_offset``                       | When the memory type in the containing struct                            |
    |                                      |                                      |                                      | :ref:`v4l2_buffer   <v4l2-buffer>`  is ``V4L2_MEMORY_MMAP``, this is the |
    |                                      |                                      |                                      | value that should be passed to :ref:`mmap()  <func-mmap>`,  similar to   |
    |                                      |                                      |                                      | the ``offset`` field in struct :ref:`v4l2_buffer   <v4l2-buffer>`.       |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------------------------------------------+
    |                                      | unsigned long                        | ``userptr``                          | When the memory type in the containing struct                            |
    |                                      |                                      |                                      | :ref:`v4l2_buffer   <v4l2-buffer>`  is ``V4L2_MEMORY_USERPTR``, this is  |
    |                                      |                                      |                                      | a userspace pointer to the memory allocated for this plane by an         |
    |                                      |                                      |                                      | application.                                                             |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------------------------------------------+
    |                                      | int                                  | ``fd``                               | When the memory type in the containing struct                            |
    |                                      |                                      |                                      | :ref:`v4l2_buffer   <v4l2-buffer>`  is ``V4L2_MEMORY_DMABUF``, this is a |
    |                                      |                                      |                                      | file descriptor associated with a DMABUF buffer, similar to the ``fd``   |
    |                                      |                                      |                                      | field in struct :ref:`v4l2_buffer   <v4l2-buffer>`.                      |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------------------------------------------+
    | __u32                                | ``data_offset``                      |                                      | Offset in bytes to video data in the plane. Drivers must set this field  |
    |                                      |                                      |                                      | when ``type`` refers to a capture stream, applications when it refers to |
    |                                      |                                      |                                      | an output stream. Note that data_offset  is included in ``bytesused``.   |
    |                                      |                                      |                                      | So the size of the image in the plane is ``bytesused``-``data_offset``   |
    |                                      |                                      |                                      | at offset ``data_offset`` from the start of the plane.                   |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------------------------------------------+
    | __u32                                | ``reserved[11]``                     |                                      | Reserved for future use. Should be zeroed by drivers and applications.   |
    +--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------------------------------------------+



.. _v4l2-buf-type:

.. table:: enum v4l2_buf_type

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_VIDEO_CAPTURE``                                     | 1                      | Buffer of a single-planar video capture stream, see :ref:`capture`.                        |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE``                              | 9                      | Buffer of a multi-planar video capture stream, see :ref:`capture`.                         |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_VIDEO_OUTPUT``                                      | 2                      | Buffer of a single-planar video output stream, see :ref:`output`.                          |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE``                               | 10                     | Buffer of a multi-planar video output stream, see :ref:`output`.                           |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_VIDEO_OVERLAY``                                     | 3                      | Buffer for video overlay, see :ref:`overlay`.                                              |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_VBI_CAPTURE``                                       | 4                      | Buffer of a raw VBI capture stream, see :ref:`raw-vbi`.                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_VBI_OUTPUT``                                        | 5                      | Buffer of a raw VBI output stream, see :ref:`raw-vbi`.                                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_SLICED_VBI_CAPTURE``                                | 6                      | Buffer of a sliced VBI capture stream, see :ref:`sliced`.                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_SLICED_VBI_OUTPUT``                                 | 7                      | Buffer of a sliced VBI output stream, see :ref:`sliced`.                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_VIDEO_OUTPUT_OVERLAY``                              | 8                      | Buffer for video output overlay (OSD), see :ref:`osd`.                                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_SDR_CAPTURE``                                       | 11                     | Buffer for Software Defined Radio (SDR) capture stream, see :ref:`sdr`.                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_TYPE_SDR_OUTPUT``                                        | 12                     | Buffer for Software Defined Radio (SDR) output stream, see :ref:`sdr`.                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



.. _buffer-flags:

.. table:: Buffer Flags

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_MAPPED``                                            | 0x00000001             | The buffer resides in device memory and has been mapped into the application's address     |
    |                                                                     |                        | space, see :ref:`mmap`   for details. Drivers set or clear this flag when the              |
    |                                                                     |                        | :ref:`VIDIOC_QUERYBUF   <vidioc-querybuf>`,  :ref:`VIDIOC_QBUF   <vidioc-qbuf>`  or        |
    |                                                                     |                        | :ref:`VIDIOC_DQBUF   <vidioc-qbuf>`  ioctl is called. Set by the driver.                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_QUEUED``                                            | 0x00000002             | Internally drivers maintain two buffer queues, an incoming and outgoing queue. When this   |
    |                                                                     |                        | flag is set, the buffer is currently on the incoming queue. It automatically moves to the  |
    |                                                                     |                        | outgoing queue after the buffer has been filled (capture devices) or displayed (output     |
    |                                                                     |                        | devices). Drivers set or clear this flag when the ``VIDIOC_QUERYBUF`` ioctl is called.     |
    |                                                                     |                        | After (successful) calling the ``VIDIOC_QBUF``\ ioctl it is always set and after           |
    |                                                                     |                        | ``VIDIOC_DQBUF`` always cleared.                                                           |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_DONE``                                              | 0x00000004             | When this flag is set, the buffer is currently on the outgoing queue, ready to be dequeued |
    |                                                                     |                        | from the driver. Drivers set or clear this flag when the ``VIDIOC_QUERYBUF`` ioctl is      |
    |                                                                     |                        | called. After calling the ``VIDIOC_QBUF`` or ``VIDIOC_DQBUF`` it is always cleared. Of     |
    |                                                                     |                        | course a buffer cannot be on both queues at the same time, the ``V4L2_BUF_FLAG_QUEUED``    |
    |                                                                     |                        | and ``V4L2_BUF_FLAG_DONE`` flag are mutually exclusive. They can be both cleared however,  |
    |                                                                     |                        | then the buffer is in "dequeued" state, in the application domain so to say.               |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_ERROR``                                             | 0x00000040             | When this flag is set, the buffer has been dequeued successfully, although the data might  |
    |                                                                     |                        | have been corrupted. This is recoverable, streaming may continue as normal and the buffer  |
    |                                                                     |                        | may be reused normally. Drivers set this flag when the ``VIDIOC_DQBUF`` ioctl is called.   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_KEYFRAME``                                          | 0x00000008             | Drivers set or clear this flag when calling the ``VIDIOC_DQBUF`` ioctl. It may be set by   |
    |                                                                     |                        | video capture devices when the buffer contains a compressed image which is a key frame (or |
    |                                                                     |                        | field), i. e. can be decompressed on its own. Also known as an I-frame. Applications can   |
    |                                                                     |                        | set this bit when ``type`` refers to an output stream.                                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_PFRAME``                                            | 0x00000010             | Similar to ``V4L2_BUF_FLAG_KEYFRAME`` this flags predicted frames or fields which contain  |
    |                                                                     |                        | only differences to a previous key frame. Applications can set this bit when ``type``      |
    |                                                                     |                        | refers to an output stream.                                                                |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_BFRAME``                                            | 0x00000020             | Similar to ``V4L2_BUF_FLAG_KEYFRAME`` this flags a bi-directional predicted frame or field |
    |                                                                     |                        | which contains only the differences between the current frame and both the preceding and   |
    |                                                                     |                        | following key frames to specify its content. Applications can set this bit when ``type``   |
    |                                                                     |                        | refers to an output stream.                                                                |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_TIMECODE``                                          | 0x00000100             | The ``timecode`` field is valid. Drivers set or clear this flag when the ``VIDIOC_DQBUF``  |
    |                                                                     |                        | ioctl is called. Applications can set this bit and the corresponding ``timecode``          |
    |                                                                     |                        | structure when ``type`` refers to an output stream.                                        |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_PREPARED``                                          | 0x00000400             | The buffer has been prepared for I/O and can be queued by the application. Drivers set or  |
    |                                                                     |                        | clear this flag when the :ref:`VIDIOC_QUERYBUF   <vidioc-querybuf>`,                       |
    |                                                                     |                        | :ref:`VIDIOC_PREPARE_BUF    <vidioc-qbuf>`,  :ref:`VIDIOC_QBUF   <vidioc-qbuf>`  or        |
    |                                                                     |                        | :ref:`VIDIOC_DQBUF   <vidioc-qbuf>`  ioctl is called.                                      |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_NO_CACHE_INVALIDATE``                               | 0x00000800             | Caches do not have to be invalidated for this buffer. Typically applications shall use     |
    |                                                                     |                        | this flag if the data captured in the buffer is not going to be touched by the CPU,        |
    |                                                                     |                        | instead the buffer will, probably, be passed on to a DMA-capable hardware unit for further |
    |                                                                     |                        | processing or output.                                                                      |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_NO_CACHE_CLEAN``                                    | 0x00001000             | Caches do not have to be cleaned for this buffer. Typically applications shall use this    |
    |                                                                     |                        | flag for output buffers if the data in this buffer has not been created by the CPU but by  |
    |                                                                     |                        | some DMA-capable unit, in which case caches have not been used.                            |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_LAST``                                              | 0x00100000             | Last buffer produced by the hardware. mem2mem codec drivers set this flag on the capture   |
    |                                                                     |                        | queue for the last buffer when the :ref:`VIDIOC_QUERYBUF   <vidioc-querybuf>`  or          |
    |                                                                     |                        | :ref:`VIDIOC_DQBUF   <vidioc-qbuf>`  ioctl is called. Due to hardware limitations, the     |
    |                                                                     |                        | last buffer may be empty. In this case the driver will set the ``bytesused`` field to 0,   |
    |                                                                     |                        | regardless of the format. Any Any subsequent call to the                                   |
    |                                                                     |                        | :ref:`VIDIOC_DQBUF   <vidioc-qbuf>`  ioctl will not block anymore, but return an EPIPE     |
    |                                                                     |                        | error code.                                                                                |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_TIMESTAMP_MASK``                                    | 0x0000e000             | Mask for timestamp types below. To test the timestamp type, mask out bits not belonging to |
    |                                                                     |                        | timestamp type by performing a logical and operation with buffer flags and timestamp mask. |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_TIMESTAMP_UNKNOWN``                                 | 0x00000000             | Unknown timestamp type. This type is used by drivers before Linux 3.9 and may be either    |
    |                                                                     |                        | monotonic (see below) or realtime (wall clock). Monotonic clock has been favoured in       |
    |                                                                     |                        | embedded systems whereas most of the drivers use the realtime clock. Either kinds of       |
    |                                                                     |                        | timestamps are available in user space via ``clock_gettime(2)`` using clock IDs            |
    |                                                                     |                        | ``CLOCK_MONOTONIC`` and ``CLOCK_REALTIME``, respectively.                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_TIMESTAMP_MONOTONIC``                               | 0x00002000             | The buffer timestamp has been taken from the ``CLOCK_MONOTONIC`` clock. To access the same |
    |                                                                     |                        | clock outside V4L2, use ``clock_gettime(2)``.                                              |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_TIMESTAMP_COPY``                                    | 0x00004000             | The CAPTURE buffer timestamp has been taken from the corresponding OUTPUT buffer. This     |
    |                                                                     |                        | flag applies only to mem2mem devices.                                                      |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_TSTAMP_SRC_MASK``                                   | 0x00070000             | Mask for timestamp sources below. The timestamp source defines the point of time the       |
    |                                                                     |                        | timestamp is taken in relation to the frame. Logical 'and' operation between the ``flags`` |
    |                                                                     |                        | field and ``V4L2_BUF_FLAG_TSTAMP_SRC_MASK`` produces the value of the timestamp source.    |
    |                                                                     |                        | Applications must set the timestamp source when ``type`` refers to an output stream and    |
    |                                                                     |                        | ``V4L2_BUF_FLAG_TIMESTAMP_COPY`` is set.                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_TSTAMP_SRC_EOF``                                    | 0x00000000             | End Of Frame. The buffer timestamp has been taken when the last pixel of the frame has     |
    |                                                                     |                        | been received or the last pixel of the frame has been transmitted. In practice, software   |
    |                                                                     |                        | generated timestamps will typically be read from the clock a small amount of time after    |
    |                                                                     |                        | the last pixel has been received or transmitten, depending on the system and other         |
    |                                                                     |                        | activity in it.                                                                            |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_BUF_FLAG_TSTAMP_SRC_SOE``                                    | 0x00010000             | Start Of Exposure. The buffer timestamp has been taken when the exposure of the frame has  |
    |                                                                     |                        | begun. This is only valid for the ``V4L2_BUF_TYPE_VIDEO_CAPTURE`` buffer type.             |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-memory:

.. table:: enum v4l2_memory

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_MEMORY_MMAP``                                                | 1                      | The buffer is used for :ref:`memory  mapping <mmap>`  I/O.                                 |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_MEMORY_USERPTR``                                             | 2                      | The buffer is used for :ref:`user  pointer <userp>`  I/O.                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_MEMORY_OVERLAY``                                             | 3                      | [to do]                                                                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_MEMORY_DMABUF``                                              | 4                      | The buffer is used for :ref:`DMA  shared buffer <dmabuf>`  I/O.                            |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



Timecodes
=========

The ``v4l2_timecode`` structure is designed to hold a :ref:`smpte12m` or similar timecode. (struct ``timeval`` timestamps are stored in struct :ref:`v4l2_buffer <v4l2-buffer>`
field ``timestamp``.)


.. _v4l2-timecode:

.. table:: struct v4l2_timecode

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``type``                                      | Frame rate the timecodes are based on, see :ref:`timecode-type`.                           |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``flags``                                     | Timecode flags, see :ref:`timecode-flags`.                                                 |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``frames``                                    | Frame count, 0 ... 23/24/29/49/59, depending on the type of timecode.                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``seconds``                                   | Seconds count, 0 ... 59. This is a binary, not BCD number.                                 |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``minutes``                                   | Minutes count, 0 ... 59. This is a binary, not BCD number.                                 |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``hours``                                     | Hours count, 0 ... 29. This is a binary, not BCD number.                                   |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``userbits``  [4]                             | The "user group" bits from the timecode.                                                   |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _timecode-type:

.. table:: Timecode Types

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_TC_TYPE_24FPS``                                              | 1                      | 24 frames per second, i. e. film.                                                          |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_TC_TYPE_25FPS``                                              | 2                      | 25 frames per second, i. e. PAL or SECAM video.                                            |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_TC_TYPE_30FPS``                                              | 3                      | 30 frames per second, i. e. NTSC video.                                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_TC_TYPE_50FPS``                                              | 4                      |                                                                                            |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_TC_TYPE_60FPS``                                              | 5                      |                                                                                            |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



.. _timecode-flags:

.. table:: Timecode Flags

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_TC_FLAG_DROPFRAME``                                          | 0x0001                 | Indicates "drop frame" semantics for counting frames in 29.97 fps material. When set,      |
    |                                                                     |                        | frame numbers 0 and 1 at the start of each minute, except minutes 0, 10, 20, 30, 40, 50    |
    |                                                                     |                        | are omitted from the count.                                                                |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_TC_FLAG_COLORFRAME``                                         | 0x0002                 | The "color frame" flag.                                                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_TC_USERBITS_field``                                          | 0x000C                 | Field mask for the "binary group flags".                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_TC_USERBITS_USERDEFINED``                                    | 0x0000                 | Unspecified format.                                                                        |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_TC_USERBITS_8BITCHARS``                                      | 0x0008                 | 8-bit ISO characters.                                                                      |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



.. _field-order:

Field Order
===========

We have to distinguish between progressive and interlaced video. Progressive video transmits all lines of a video image sequentially. Interlaced video divides an image into two
fields, containing only the odd and even lines of the image, respectively. Alternating the so called odd and even field are transmitted, and due to a small delay between fields a
cathode ray TV displays the lines interleaved, yielding the original frame. This curious technique was invented because at refresh rates similar to film the image would fade out
too quickly. Transmitting fields reduces the flicker without the necessity of doubling the frame rate and with it the bandwidth required for each channel.

It is important to understand a video camera does not expose one frame at a time, merely transmitting the frames separated into fields. The fields are in fact captured at two
different instances in time. An object on screen may well move between one field and the next. For applications analysing motion it is of paramount importance to recognize which
field of a frame is older, the *temporal order*.

When the driver provides or accepts images field by field rather than interleaved, it is also important applications understand how the fields combine to frames. We distinguish
between top (aka odd) and bottom (aka even) fields, the *spatial order*: The first line of the top field is the first line of an interlaced frame, the first line of the bottom
field is the second line of that frame.

However because fields were captured one after the other, arguing whether a frame commences with the top or bottom field is pointless. Any two successive top and bottom, or bottom
and top fields yield a valid frame. Only when the source was progressive to begin with, e. g. when transferring film to video, two fields may come from the same frame, creating a
natural order.

Counter to intuition the top field is not necessarily the older field. Whether the older field contains the top or bottom lines is a convention determined by the video standard.
Hence the distinction between temporal and spatial order of fields. The diagrams below should make this clearer.

All video capture and output devices must report the current field order. Some drivers may permit the selection of a different order, to this end applications initialize the
``field`` field of struct :ref:`v4l2_pix_format <v4l2-pix-format>` before calling the :ref:`VIDIOC_S_FMT <vidioc-g-fmt>` ioctl. If this is not desired it should have the
value ``V4L2_FIELD_ANY`` (0).


.. _v4l2-field:

.. table:: enum v4l2_field

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FIELD_ANY``                                                  | 0                      | Applications request this field order when any one of the ``V4L2_FIELD_NONE``,             |
    |                                                                     |                        | ``V4L2_FIELD_TOP``, ``V4L2_FIELD_BOTTOM``, or ``V4L2_FIELD_INTERLACED`` formats is         |
    |                                                                     |                        | acceptable. Drivers choose depending on hardware capabilities or e. g. the requested image |
    |                                                                     |                        | size, and return the actual field order. Drivers must never return ``V4L2_FIELD_ANY``. If  |
    |                                                                     |                        | multiple field orders are possible the driver must choose one of the possible field orders |
    |                                                                     |                        | during :ref:`VIDIOC_S_FMT    <vidioc-g-fmt>`  or :ref:`VIDIOC_TRY_FMT    <vidioc-g-fmt>`.  |
    |                                                                     |                        | struct :ref:`v4l2_buffer   <v4l2-buffer>`  ``field`` can never be ``V4L2_FIELD_ANY``.      |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FIELD_NONE``                                                 | 1                      | Images are in progressive format, not interlaced. The driver may also indicate this order  |
    |                                                                     |                        | when it cannot distinguish between ``V4L2_FIELD_TOP`` and ``V4L2_FIELD_BOTTOM``.           |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FIELD_TOP``                                                  | 2                      | Images consist of the top (aka odd) field only.                                            |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FIELD_BOTTOM``                                               | 3                      | Images consist of the bottom (aka even) field only. Applications may wish to prevent a     |
    |                                                                     |                        | device from capturing interlaced images because they will have "comb" or "feathering"      |
    |                                                                     |                        | artefacts around moving objects.                                                           |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FIELD_INTERLACED``                                           | 4                      | Images contain both fields, interleaved line by line. The temporal order of the fields     |
    |                                                                     |                        | (whether the top or bottom field is first transmitted) depends on the current video        |
    |                                                                     |                        | standard. M/NTSC transmits the bottom field first, all other standards the top field       |
    |                                                                     |                        | first.                                                                                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FIELD_SEQ_TB``                                               | 5                      | Images contain both fields, the top field lines are stored first in memory, immediately    |
    |                                                                     |                        | followed by the bottom field lines. Fields are always stored in temporal order, the older  |
    |                                                                     |                        | one first in memory. Image sizes refer to the frame, not fields.                           |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FIELD_SEQ_BT``                                               | 6                      | Images contain both fields, the bottom field lines are stored first in memory, immediately |
    |                                                                     |                        | followed by the top field lines. Fields are always stored in temporal order, the older one |
    |                                                                     |                        | first in memory. Image sizes refer to the frame, not fields.                               |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FIELD_ALTERNATE``                                            | 7                      | The two fields of a frame are passed in separate buffers, in temporal order, i. e. the     |
    |                                                                     |                        | older one first. To indicate the field parity (whether the current field is a top or       |
    |                                                                     |                        | bottom field) the driver or application, depending on data direction, must set struct      |
    |                                                                     |                        | :ref:`v4l2_buffer   <v4l2-buffer>`  ``field`` to ``V4L2_FIELD_TOP`` or                     |
    |                                                                     |                        | ``V4L2_FIELD_BOTTOM``. Any two successive fields pair to build a frame. If fields are      |
    |                                                                     |                        | successive, without any dropped fields between them (fields can drop individually), can be |
    |                                                                     |                        | determined from the struct :ref:`v4l2_buffer   <v4l2-buffer>`  ``sequence`` field. This    |
    |                                                                     |                        | format cannot be selected when using the read/write I/O method since there is no way to    |
    |                                                                     |                        | communicate if a field was a top or bottom field.                                          |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FIELD_INTERLACED_TB``                                        | 8                      | Images contain both fields, interleaved line by line, top field first. The top field is    |
    |                                                                     |                        | transmitted first.                                                                         |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FIELD_INTERLACED_BT``                                        | 9                      | Images contain both fields, interleaved line by line, top field first. The bottom field is |
    |                                                                     |                        | transmitted first.                                                                         |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



.. _fieldseq-tb:

.. figure::  io_files/fieldseq_tb.*
    :alt:    fieldseq_tb.pdf / fieldseq_tb.gif
    :align:  center

    Field Order, Top Field First Transmitted


.. _fieldseq-bt:

.. figure::  io_files/fieldseq_bt.*
    :alt:    fieldseq_bt.pdf / fieldseq_bt.gif
    :align:  center

    Field Order, Bottom Field First Transmitted

.. [1]
   It would be desirable if applications could depend on drivers supporting all I/O interfaces, but as much as the complex memory mapping I/O can be inadequate for some devices we
   have no reason to require this interface, which is most useful for simple applications capturing still images.

.. [2]
   At the driver level ``select()`` and ``poll()`` are the same, and ``select()`` is too important to be optional.

.. [3]
   One could use one file descriptor and set the buffer type field accordingly when calling :ref:`VIDIOC_QBUF <vidioc-qbuf>` etc., but it makes the ``select()`` function
   ambiguous. We also like the clean approach of one file descriptor per logical stream. Video overlay for example is also a logical stream, although the CPU is not needed for
   continuous operation.

.. [4]
   Random enqueue order permits applications processing images out of order (such as video codecs) to return buffers earlier, reducing the probability of data loss. Random fill
   order allows drivers to reuse buffers on a LIFO-basis, taking advantage of caches holding scatter-gather lists and the like.

.. [5]
   At the driver level ``select()`` and ``poll()`` are the same, and ``select()`` is too important to be optional. The rest should be evident.

.. [6]
   We expect that frequently used buffers are typically not swapped out. Anyway, the process of swapping, locking or generating scatter-gather lists may be time consuming. The
   delay can be masked by the depth of the incoming buffer queue, and perhaps by maintaining caches assuming a buffer will be soon enqueued again. On the other hand, to optimize
   memory usage drivers can limit the number of buffers locked in advance and recycle the most recently used buffers first. Of course, the pages of empty buffers in the incoming
   queue need not be saved to disk. Output buffers must be saved on the incoming and outgoing queue because an application may share them with other processes.

.. [7]
   At the driver level ``select()`` and ``poll()`` are the same, and ``select()`` is too important to be optional. The rest should be evident.
