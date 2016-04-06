
.. _vidioc-subscribe-event:

======================================================
ioctl VIDIOC_SUBSCRIBE_EVENT, VIDIOC_UNSUBSCRIBE_EVENT
======================================================

*man VIDIOC_SUBSCRIBE_EVENT(2)*

VIDIOC_UNSUBSCRIBE_EVENT
Subscribe or unsubscribe event


Synopsis
========

.. c:function:: int ioctl( int fd, int request, struct v4l2_event_subscription *argp )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <func-open>`.

``request``
    VIDIOC_SUBSCRIBE_EVENT, VIDIOC_UNSUBSCRIBE_EVENT

``argp``


Description
===========

Subscribe or unsubscribe V4L2 event. Subscribed events are dequeued by using the :ref:`VIDIOC_DQEVENT <vidioc-dqevent>` ioctl.


.. _v4l2-event-subscription:

.. table:: struct v4l2_event_subscription

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``type``                                      | Type of the event, see :ref:`event-type`.   Note that ``V4L2_EVENT_ALL`` can be used with  |
    |                                               |                                               | VIDIOC_UNSUBSCRIBE_EVENT   for unsubscribing all events at once.                           |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``id``                                        | ID of the event source. If there is no ID associated with the event source, then set this  |
    |                                               |                                               | to 0. Whether or not an event needs an ID depends on the event type.                       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``flags``                                     | Event flags, see :ref:`event-flags`.                                                       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``reserved``  [5]                             | Reserved for future extensions. Drivers and applications must set the array to zero.       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _event-flags:

.. table:: Event Flags

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_SUB_FL_SEND_INITIAL``                                  | 0x0001                 | When this event is subscribed an initial event will be sent containing the current status. |
    |                                                                     |                        | This only makes sense for events that are triggered by a status change such as             |
    |                                                                     |                        | ``V4L2_EVENT_CTRL``. Other events will ignore this flag.                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_EVENT_SUB_FL_ALLOW_FEEDBACK``                                | 0x0002                 | If set, then events directly caused by an ioctl will also be sent to the filehandle that   |
    |                                                                     |                        | called that ioctl. For example, changing a control using                                   |
    |                                                                     |                        | :ref:`VIDIOC_S_CTRL    <vidioc-g-ctrl>`  will cause a V4L2_EVENT_CTRL   to be sent back to |
    |                                                                     |                        | that same filehandle. Normally such events are suppressed to prevent feedback loops where  |
    |                                                                     |                        | an application changes a control to a one value and then another, and then receives an     |
    |                                                                     |                        | event telling it that that control has changed to the first value.                         |
    |                                                                     |                        |                                                                                            |
    |                                                                     |                        | Since it can't tell whether that event was caused by another application or by the         |
    |                                                                     |                        | :ref:`VIDIOC_S_CTRL    <vidioc-g-ctrl>`  call it is hard to decide whether to set the      |
    |                                                                     |                        | control to the value in the event, or ignore it.                                           |
    |                                                                     |                        |                                                                                            |
    |                                                                     |                        | Think carefully when you set this flag so you won't get into situations like that.         |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



Return Value
============

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.
