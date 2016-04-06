
.. _vidioc-dqevent:

====================
ioctl VIDIOC_DQEVENT
====================

*man VIDIOC_DQEVENT(2)*

Dequeue event


Synopsis
========

.. c:function:: int ioctl( int fd, int request, struct v4l2_event *argp )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <func-open>`.

``request``
    VIDIOC_DQEVENT

``argp``


Description
===========

Dequeue an event from a video device. No input is required for this ioctl. All the fields of the struct :ref:`v4l2_event <v4l2-event>` structure are filled by the driver. The
file handle will also receive exceptions which the application may get by e.g. using the select system call.


.. _v4l2-event:

.. table:: struct v4l2_event

    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __u32                                         | ``type``                                      |                                               | Type of the event, see :ref:`event-type`.     |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | union                                         | ``u``                                         |                                               |                                               |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    |                                               | struct                                        | ``vsync``                                     | Event data for event ``V4L2_EVENT_VSYNC``.    |
    |                                               | :ref:`v4l2_event_vsync    <v4l2-event-vsync>  |                                               |                                               |
    |                                               | `                                             |                                               |                                               |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    |                                               | struct                                        | ``ctrl``                                      | Event data for event ``V4L2_EVENT_CTRL``.     |
    |                                               | :ref:`v4l2_event_ctrl    <v4l2-event-ctrl>`   |                                               |                                               |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    |                                               | struct                                        | ``frame_sync``                                | Event data for event                          |
    |                                               | :ref:`v4l2_event_frame_sync     <v4l2-event-f |                                               | ``V4L2_EVENT_FRAME_SYNC``.                    |
    |                                               | rame-sync>`                                   |                                               |                                               |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    |                                               | struct                                        | ``motion_det``                                | Event data for event                          |
    |                                               | :ref:`v4l2_event_motion_det     <v4l2-event-m |                                               | V4L2_EVENT_MOTION_DET.                        |
    |                                               | otion-det>`                                   |                                               |                                               |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    |                                               | struct                                        | ``src_change``                                | Event data for event                          |
    |                                               | :ref:`v4l2_event_src_change     <v4l2-event-s |                                               | V4L2_EVENT_SOURCE_CHANGE.                     |
    |                                               | rc-change>`                                   |                                               |                                               |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    |                                               | __u8                                          | ``data``  [64]                                | Event data. Defined by the event type. The    |
    |                                               |                                               |                                               | union should be used to define easily         |
    |                                               |                                               |                                               | accessible type for events.                   |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __u32                                         | ``pending``                                   |                                               | Number of pending events excluding this one.  |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __u32                                         | ``sequence``                                  |                                               | Event sequence number. The sequence number is |
    |                                               |                                               |                                               | incremented for every subscribed event that   |
    |                                               |                                               |                                               | takes place. If sequence numbers are not      |
    |                                               |                                               |                                               | contiguous it means that events have been     |
    |                                               |                                               |                                               | lost.                                         |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | struct timespec                               | ``timestamp``                                 |                                               | Event timestamp. The timestamp has been taken |
    |                                               |                                               |                                               | from the ``CLOCK_MONOTONIC`` clock. To access |
    |                                               |                                               |                                               | the same clock outside V4L2, use              |
    |                                               |                                               |                                               | ``clock_gettime(2)``.                         |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | u32                                           | ``id``                                        |                                               | The ID associated with the event source. If   |
    |                                               |                                               |                                               | the event does not have an associated ID      |
    |                                               |                                               |                                               | (this depends on the event type), then this   |
    |                                               |                                               |                                               | is 0.                                         |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __u32                                         | ``reserved``  [8]                             |                                               | Reserved for future extensions. Drivers must  |
    |                                               |                                               |                                               | set the array to zero.                        |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+



.. _event-type:

.. table:: Event Types

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_ALL``                                                  | 0                      | All events. V4L2_EVENT_ALL   is valid only for VIDIOC_UNSUBSCRIBE_EVENT   for              |
    |                                                                     |                        | unsubscribing all events at once.                                                          |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_VSYNC``                                                | 1                      | This event is triggered on the vertical sync. This event has a struct                      |
    |                                                                     |                        | :ref:`v4l2_event_vsync    <v4l2-event-vsync>`  associated with it.                         |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_EOS``                                                  | 2                      | This event is triggered when the end of a stream is reached. This is typically used with   |
    |                                                                     |                        | MPEG decoders to report to the application when the last of the MPEG stream has been       |
    |                                                                     |                        | decoded.                                                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_CTRL``                                                 | 3                      | This event requires that the ``id`` matches the control ID from which you want to receive  |
    |                                                                     |                        | events. This event is triggered if the control's value changes, if a button control is     |
    |                                                                     |                        | pressed or if the control's flags change. This event has a struct                          |
    |                                                                     |                        | :ref:`v4l2_event_ctrl    <v4l2-event-ctrl>`  associated with it. This struct contains much |
    |                                                                     |                        | of the same information as struct :ref:`v4l2_queryctrl   <v4l2-queryctrl>`  and struct     |
    |                                                                     |                        | :ref:`v4l2_control   <v4l2-control>`.                                                      |
    |                                                                     |                        |                                                                                            |
    |                                                                     |                        | If the event is generated due to a call to :ref:`VIDIOC_S_CTRL    <vidioc-g-ctrl>`  or     |
    |                                                                     |                        | :ref:`VIDIOC_S_EXT_CTRLS     <vidioc-g-ext-ctrls>`,  then the event will *not* be sent to  |
    |                                                                     |                        | the file handle that called the ioctl function. This prevents nasty feedback loops. If you |
    |                                                                     |                        | *do* want to get the event, then set the ``V4L2_EVENT_SUB_FL_ALLOW_FEEDBACK`` flag.        |
    |                                                                     |                        |                                                                                            |
    |                                                                     |                        | This event type will ensure that no information is lost when more events are raised than   |
    |                                                                     |                        | there is room internally. In that case the struct                                          |
    |                                                                     |                        | :ref:`v4l2_event_ctrl    <v4l2-event-ctrl>`  of the second-oldest event is kept, but the   |
    |                                                                     |                        | ``changes`` field of the second-oldest event is ORed with the ``changes`` field of the     |
    |                                                                     |                        | oldest event.                                                                              |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_FRAME_SYNC``                                           | 4                      | Triggered immediately when the reception of a frame has begun. This event has a struct     |
    |                                                                     |                        | :ref:`v4l2_event_frame_sync     <v4l2-event-frame-sync>`  associated with it.              |
    |                                                                     |                        |                                                                                            |
    |                                                                     |                        | If the hardware needs to be stopped in the case of a buffer underrun it might not be able  |
    |                                                                     |                        | to generate this event. In such cases the ``frame_sequence`` field in struct               |
    |                                                                     |                        | :ref:`v4l2_event_frame_sync     <v4l2-event-frame-sync>`  will not be incremented. This    |
    |                                                                     |                        | causes two consecutive frame sequence numbers to have n times frame interval in between    |
    |                                                                     |                        | them.                                                                                      |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_SOURCE_CHANGE``                                        | 5                      | This event is triggered when a source parameter change is detected during runtime by the   |
    |                                                                     |                        | video device. It can be a runtime resolution change triggered by a video decoder or the    |
    |                                                                     |                        | format change happening on an input connector. This event requires that the ``id`` matches |
    |                                                                     |                        | the input index (when used with a video device node) or the pad index (when used with a    |
    |                                                                     |                        | subdevice node) from which you want to receive events.                                     |
    |                                                                     |                        |                                                                                            |
    |                                                                     |                        | This event has a struct :ref:`v4l2_event_src_change     <v4l2-event-src-change>`           |
    |                                                                     |                        | associated with it. The ``changes`` bitfield denotes what has changed for the subscribed   |
    |                                                                     |                        | pad. If multiple events occurred before application could dequeue them, then the changes   |
    |                                                                     |                        | will have the ORed value of all the events generated.                                      |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_MOTION_DET``                                           | 6                      | Triggered whenever the motion detection state for one or more of the regions changes. This |
    |                                                                     |                        | event has a struct :ref:`v4l2_event_motion_det     <v4l2-event-motion-det>`  associated    |
    |                                                                     |                        | with it.                                                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_PRIVATE_START``                                        | 0x08000000             | Base event number for driver-private events.                                               |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-event-vsync:

.. table:: struct v4l2_event_vsync

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``field``                                     | The upcoming field. See enum :ref:`v4l2_field   <v4l2-field>`.                             |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-event-ctrl:

.. table:: struct v4l2_event_ctrl

    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __u32                                         | ``changes``                                   |                                               | A bitmask that tells what has changed. See    |
    |                                               |                                               |                                               | :ref:`ctrl-changes-flags`.                    |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __u32                                         | ``type``                                      |                                               | The type of the control. See enum             |
    |                                               |                                               |                                               | :ref:`v4l2_ctrl_type    <v4l2-ctrl-type>`.    |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | union (anonymous)                             |                                               |                                               |                                               |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    |                                               | __s32                                         | ``value``                                     | The 32-bit value of the control for 32-bit    |
    |                                               |                                               |                                               | control types. This is 0 for string controls  |
    |                                               |                                               |                                               | since the value of a string cannot be passed  |
    |                                               |                                               |                                               | using                                         |
    |                                               |                                               |                                               | :ref:`VIDIOC_DQEVENT   <vidioc-dqevent>`.     |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    |                                               | __s64                                         | ``value64``                                   | The 64-bit value of the control for 64-bit    |
    |                                               |                                               |                                               | control types.                                |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __u32                                         | ``flags``                                     |                                               | The control flags. See                        |
    |                                               |                                               |                                               | :ref:`control-flags`.                         |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __s32                                         | ``minimum``                                   |                                               | The minimum value of the control. See struct  |
    |                                               |                                               |                                               | :ref:`v4l2_queryctrl   <v4l2-queryctrl>`.     |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __s32                                         | ``maximum``                                   |                                               | The maximum value of the control. See struct  |
    |                                               |                                               |                                               | :ref:`v4l2_queryctrl   <v4l2-queryctrl>`.     |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __s32                                         | ``step``                                      |                                               | The step value of the control. See struct     |
    |                                               |                                               |                                               | :ref:`v4l2_queryctrl   <v4l2-queryctrl>`.     |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __s32                                         | ``default_value``                             |                                               | The default value value of the control. See   |
    |                                               |                                               |                                               | struct                                        |
    |                                               |                                               |                                               | :ref:`v4l2_queryctrl   <v4l2-queryctrl>`.     |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+



.. _v4l2-event-frame-sync:

.. table:: struct v4l2_event_frame_sync

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``frame_sequence``                            | The sequence number of the frame being received.                                           |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-event-src-change:

.. table:: struct v4l2_event_src_change

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``changes``                                   | A bitmask that tells what has changed. See :ref:`src-changes-flags`.                       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-event-motion-det:

.. table:: struct v4l2_event_motion_det

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``flags``                                     | Currently only one flag is available: if ``V4L2_EVENT_MD_FL_HAVE_FRAME_SEQ`` is set, then  |
    |                                               |                                               | the ``frame_sequence`` field is valid, otherwise that field should be ignored.             |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``frame_sequence``                            | The sequence number of the frame being received. Only valid if the                         |
    |                                               |                                               | ``V4L2_EVENT_MD_FL_HAVE_FRAME_SEQ`` flag was set.                                          |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``region_mask``                               | The bitmask of the regions that reported motion. There is at least one region. If this     |
    |                                               |                                               | field is 0, then no motion was detected at all. If there is no                             |
    |                                               |                                               | ``V4L2_CID_DETECT_MD_REGION_GRID`` control (see :ref:`detect-controls`)   to assign a      |
    |                                               |                                               | different region to each cell in the motion detection grid, then that all cells are        |
    |                                               |                                               | automatically assigned to the default region 0.                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _ctrl-changes-flags:

.. table:: Control Changes

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_CTRL_CH_VALUE``                                        | 0x0001                 | This control event was triggered because the value of the control changed. Special cases:  |
    |                                                                     |                        | Volatile controls do no generate this event; If a control has the                          |
    |                                                                     |                        | ``V4L2_CTRL_FLAG_EXECUTE_ON_WRITE`` flag set, then this event is sent as well, regardless  |
    |                                                                     |                        | its value.                                                                                 |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_CTRL_CH_FLAGS``                                        | 0x0002                 | This control event was triggered because the control flags changed.                        |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_CTRL_CH_RANGE``                                        | 0x0004                 | This control event was triggered because the minimum, maximum, step or the default value   |
    |                                                                     |                        | of the control changed.                                                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



.. _src-changes-flags:

.. table:: Source Changes

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_SRC_CH_RESOLUTION``                                    | 0x0001                 | This event gets triggered when a resolution change is detected at an input. This can come  |
    |                                                                     |                        | from an input connector or from a video decoder.                                           |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



Return Value
============

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.
