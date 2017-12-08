.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/hcd_queue.c

.. _`dwc2_periodic_channel_available`:

dwc2_periodic_channel_available
===============================

.. c:function:: int dwc2_periodic_channel_available(struct dwc2_hsotg *hsotg)

    Checks that a channel is available for a periodic transfer

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

.. _`dwc2_periodic_channel_available.return`:

Return
------

0 if successful, negative error code otherwise

.. _`dwc2_check_periodic_bandwidth`:

dwc2_check_periodic_bandwidth
=============================

.. c:function:: int dwc2_check_periodic_bandwidth(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Checks that there is sufficient bandwidth for the specified QH in the periodic schedule

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        QH containing periodic bandwidth required

.. _`dwc2_check_periodic_bandwidth.return`:

Return
------

0 if successful, negative error code otherwise

For simplicity, this calculation assumes that all the transfers in the
periodic schedule may occur in the same (micro)frame

.. _`pmap_schedule`:

pmap_schedule
=============

.. c:function:: int pmap_schedule(unsigned long *map, int bits_per_period, int periods_in_map, int num_bits, int interval, int start, bool only_one_period)

    Schedule time in a periodic bitmap (pmap).

    :param unsigned long \*map:
        The bitmap representing the schedule; will be updated
        upon success.

    :param int bits_per_period:
        The schedule represents several periods.  This is how many
        bits are in each period.  It's assumed that the beginning
        of the schedule will repeat after its end.

    :param int periods_in_map:
        The number of periods in the schedule.

    :param int num_bits:
        The number of bits we need per period we want to reserve
        in this function call.

    :param int interval:
        How often we need to be scheduled for the reservation this
        time.  1 means every period.  2 means every other period.
        ...you get the picture?

    :param int start:
        The bit number to start at.  Normally 0.  Must be within
        the interval or we return failure right away.

    :param bool only_one_period:
        Normally we'll allow picking a start anywhere within the
        first interval, since we can still make all repetition
        requirements by doing that.  However, if you pass true
        here then we'll return failure if we can't fit within
        the period that "start" is in.

.. _`pmap_schedule.description`:

Description
-----------

The idea here is that we want to schedule time for repeating events that all
want the same resource.  The resource is divided into fixed-sized periods
and the events want to repeat every "interval" periods.  The schedule
granularity is one bit.

To keep things "simple", we'll represent our schedule with a bitmap that
contains a fixed number of periods.  This gets rid of a lot of complexity
but does mean that we need to handle things specially (and non-ideally) if
the number of the periods in the schedule doesn't match well with the
intervals that we're trying to schedule.

Here's an explanation of the scheme we'll implement, assuming 8 periods.
- If interval is 1, we need to take up space in each of the 8
periods we're scheduling.  Easy.
- If interval is 2, we need to take up space in half of the
periods.  Again, easy.
- If interval is 3, we actually need to fall back to interval 1.
Why?  Because we might need time in any period.  AKA for the
first 8 periods, we'll be in slot 0, 3, 6.  Then we'll be
in slot 1, 4, 7.  Then we'll be in 2, 5.  Then we'll be back to
0, 3, and 6.  Since we could be in any frame we need to reserve
for all of them.  Sucks, but that's what you gotta do.  Note that
if we were instead scheduling 8 \* 3 = 24 we'd do much better, but
then we need more memory and time to do scheduling.
- If interval is 4, easy.
- If interval is 5, we again need interval 1.  The schedule will be
0, 5, 2, 7, 4, 1, 6, 3, 0
- If interval is 6, we need interval 2.  0, 6, 4, 2.
- If interval is 7, we need interval 1.
- If interval is 8, we need interval 8.

If you do the math, you'll see that we need to pretend that interval is
equal to the greatest_common_divisor(interval, periods_in_map).

Note that at the moment this function tends to front-pack the schedule.
In some cases that's really non-ideal (it's hard to schedule things that
need to repeat every period).  In other cases it's perfect (you can easily
schedule bigger, less often repeating things).

Here's the algorithm in action (8 periods, 5 bits per period):
\|\*\*   \|     \|\*\*   \|     \|\*\*   \|     \|\*\*   \|     \|   OK 2 bits, intv 2 at 0
\|\*\*\*\*\*\|  \*\*\*\|\*\*\*\*\*\|  \*\*\*\|\*\*\*\*\*\|  \*\*\*\|\*\*\*\*\*\|  \*\*\*\|   OK 3 bits, intv 3 at 2
\|\*\*\*\*\*\|\* \*\*\*\|\*\*\*\*\*\|  \*\*\*\|\*\*\*\*\*\|\* \*\*\*\|\*\*\*\*\*\|  \*\*\*\|   OK 1 bits, intv 4 at 5
\|\*\*   \|\*    \|\*\*   \|     \|\*\*   \|\*    \|\*\*   \|     \| Remv 3 bits, intv 3 at 2
\|\*\*\*  \|\*    \|\*\*\*  \|     \|\*\*\*  \|\*    \|\*\*\*  \|     \|   OK 1 bits, intv 6 at 2
\|\*\*\*\* \|\*  \* \|\*\*\*\* \|   \* \|\*\*\*\* \|\*  \* \|\*\*\*\* \|   \* \|   OK 1 bits, intv 1 at 3
\|\*\*\*\* \|\*\*\*\* \|\*\*\*\* \| \*\*\* \|\*\*\*\* \|\*\*\*\* \|\*\*\*\* \| \*\*\* \|   OK 2 bits, intv 2 at 6
\|\*\*\*\*\*\|\*\*\*\*\*\|\*\*\*\*\*\| \*\*\*\*\|\*\*\*\*\*\|\*\*\*\*\*\|\*\*\*\*\*\| \*\*\*\*\|   OK 1 bits, intv 1 at 4
\|\*\*\*\*\*\|\*\*\*\*\*\|\*\*\*\*\*\| \*\*\*\*\|\*\*\*\*\*\|\*\*\*\*\*\|\*\*\*\*\*\| \*\*\*\*\| FAIL 1 bits, intv 1
\|  \*\*\*\|\*\*\*\*\*\|  \*\*\*\| \*\*\*\*\|  \*\*\*\|\*\*\*\*\*\|  \*\*\*\| \*\*\*\*\| Remv 2 bits, intv 2 at 0
\|  \*\*\*\| \*\*\*\*\|  \*\*\*\| \*\*\*\*\|  \*\*\*\| \*\*\*\*\|  \*\*\*\| \*\*\*\*\| Remv 1 bits, intv 4 at 5
\|   \*\*\| \*\*\*\*\|   \*\*\| \*\*\*\*\|   \*\*\| \*\*\*\*\|   \*\*\| \*\*\*\*\| Remv 1 bits, intv 6 at 2
\|    \*\| \*\* \*\|    \*\| \*\* \*\|    \*\| \*\* \*\|    \*\| \*\* \*\| Remv 1 bits, intv 1 at 3
\|    \*\|    \*\|    \*\|    \*\|    \*\|    \*\|    \*\|    \*\| Remv 2 bits, intv 2 at 6
\|     \|     \|     \|     \|     \|     \|     \|     \| Remv 1 bits, intv 1 at 4
\|\*\*   \|     \|\*\*   \|     \|\*\*   \|     \|\*\*   \|     \|   OK 2 bits, intv 2 at 0
\|\*\*\*  \|     \|\*\*   \|     \|\*\*\*  \|     \|\*\*   \|     \|   OK 1 bits, intv 4 at 2
\|\*\*\*\*\*\|     \|\*\* \*\*\|     \|\*\*\*\*\*\|     \|\*\* \*\*\|     \|   OK 2 bits, intv 2 at 3
\|\*\*\*\*\*\|\*    \|\*\* \*\*\|     \|\*\*\*\*\*\|\*    \|\*\* \*\*\|     \|   OK 1 bits, intv 4 at 5
\|\*\*\*\*\*\|\*\*\*  \|\*\* \*\*\| \*\*  \|\*\*\*\*\*\|\*\*\*  \|\*\* \*\*\| \*\*  \|   OK 2 bits, intv 2 at 6
\|\*\*\*\*\*\|\*\*\*\*\*\|\*\* \*\*\| \*\*\*\*\|\*\*\*\*\*\|\*\*\*\*\*\|\*\* \*\*\| \*\*\*\*\|   OK 2 bits, intv 2 at 8
\|\*\*\*\*\*\|\*\*\*\*\*\|\*\*\*\*\*\| \*\*\*\*\|\*\*\*\*\*\|\*\*\*\*\*\|\*\*\*\*\*\| \*\*\*\*\|   OK 1 bits, intv 4 at 12

This function is pretty generic and could be easily abstracted if anything
needed similar scheduling.

Returns either -ENOSPC or a >= 0 start bit which should be passed to the
unschedule routine.  The map bitmap will be updated on a non-error result.

.. _`pmap_unschedule`:

pmap_unschedule
===============

.. c:function:: void pmap_unschedule(unsigned long *map, int bits_per_period, int periods_in_map, int num_bits, int interval, int start)

    Undo work done by \ :c:func:`pmap_schedule`\ 

    :param unsigned long \*map:
        See \ :c:func:`pmap_schedule`\ .

    :param int bits_per_period:
        See \ :c:func:`pmap_schedule`\ .

    :param int periods_in_map:
        See \ :c:func:`pmap_schedule`\ .

    :param int num_bits:
        The number of bits that was passed to schedule.

    :param int interval:
        The interval that was passed to schedule.

    :param int start:
        The return value from \ :c:func:`pmap_schedule`\ .

.. _`dwc2_get_ls_map`:

dwc2_get_ls_map
===============

.. c:function:: unsigned long *dwc2_get_ls_map(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Get the map used for the given qh

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

.. _`dwc2_get_ls_map.description`:

Description
-----------

We'll always get the periodic map out of our TT.  Note that even if we're
running the host straight in low speed / full speed mode it appears as if
a TT is allocated for us, so we'll use it.  If that ever changes we can
add logic here to get a map out of "hsotg" if !qh->do_split.

.. _`dwc2_get_ls_map.return`:

Return
------

the map or NULL if a map couldn't be found.

.. _`dwc2_qh_print`:

dwc2_qh_print
=============

.. c:function:: void dwc2_qh_print(const char *str, void *data)

    Helper function for \ :c:func:`dwc2_qh_schedule_print`\ 

    :param const char \*str:
        The string to print

    :param void \*data:
        A pointer to a struct dwc2_qh_print_data

.. _`dwc2_qh_schedule_print`:

dwc2_qh_schedule_print
======================

.. c:function:: void dwc2_qh_schedule_print(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Print the periodic schedule

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_qh \*qh:
        QH to print.

.. _`dwc2_ls_pmap_schedule`:

dwc2_ls_pmap_schedule
=====================

.. c:function:: int dwc2_ls_pmap_schedule(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh, int search_slice)

    Schedule a low speed QH

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

    :param int search_slice:
        We'll start trying to schedule at the passed slice.
        Remember that slices are the units of the low speed
        schedule (think 25us or so).

.. _`dwc2_ls_pmap_schedule.description`:

Description
-----------

Wraps \ :c:func:`pmap_schedule`\  with the right parameters for low speed scheduling.

Normally we schedule low speed devices on the map associated with the TT.

.. _`dwc2_ls_pmap_schedule.return`:

Return
------

0 for success or an error code.

.. _`dwc2_ls_pmap_unschedule`:

dwc2_ls_pmap_unschedule
=======================

.. c:function:: void dwc2_ls_pmap_unschedule(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Undo work done by \ :c:func:`dwc2_ls_pmap_schedule`\ 

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

.. _`dwc2_hs_pmap_schedule`:

dwc2_hs_pmap_schedule
=====================

.. c:function:: int dwc2_hs_pmap_schedule(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh, bool only_one_period, int index)

    Schedule in the main high speed schedule

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

    :param bool only_one_period:
        If true we will limit ourselves to just looking at
        one period (aka one 100us chunk).  This is used if we have
        already scheduled something on the low speed schedule and
        need to find something that matches on the high speed one.

    :param int index:
        The index into qh->hs_transfers that we're working with.

.. _`dwc2_hs_pmap_schedule.description`:

Description
-----------

This will schedule something on the main dwc2 schedule.

We'll start looking in qh->hs_transfers[index].start_schedule_us.  We'll
update this with the result upon success.  We also use the duration from
the same structure.

.. _`dwc2_hs_pmap_schedule.return`:

Return
------

0 for success or an error code.  Upon success the
dwc2_hs_transfer_time specified by "index" will be updated.

.. _`dwc2_hs_pmap_unschedule`:

dwc2_hs_pmap_unschedule
=======================

.. c:function:: void dwc2_hs_pmap_unschedule(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh, int index)

    Undo work done by \ :c:func:`dwc2_hs_pmap_schedule`\ 

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

    :param int index:
        *undescribed*

.. _`dwc2_uframe_schedule_split`:

dwc2_uframe_schedule_split
==========================

.. c:function:: int dwc2_uframe_schedule_split(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Schedule a QH for a periodic split xfer.

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

.. _`dwc2_uframe_schedule_split.description`:

Description
-----------

This is the most complicated thing in USB.  We have to find matching time
in both the global high speed schedule for the port and the low speed
schedule for the TT associated with the given device.

Being here means that the host must be running in high speed mode and the
device is in low or full speed mode (and behind a hub).

.. _`dwc2_uframe_schedule_hs`:

dwc2_uframe_schedule_hs
=======================

.. c:function:: int dwc2_uframe_schedule_hs(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Schedule a QH for a periodic high speed xfer.

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

.. _`dwc2_uframe_schedule_hs.description`:

Description
-----------

Basically this just wraps \ :c:func:`dwc2_hs_pmap_schedule`\  to provide a clean
interface.

.. _`dwc2_uframe_schedule_ls`:

dwc2_uframe_schedule_ls
=======================

.. c:function:: int dwc2_uframe_schedule_ls(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Schedule a QH for a periodic low/full speed xfer.

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

.. _`dwc2_uframe_schedule_ls.description`:

Description
-----------

Basically this just wraps \ :c:func:`dwc2_ls_pmap_schedule`\  to provide a clean
interface.

.. _`dwc2_uframe_schedule`:

dwc2_uframe_schedule
====================

.. c:function:: int dwc2_uframe_schedule(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Schedule a QH for a periodic xfer.

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

.. _`dwc2_uframe_schedule.description`:

Description
-----------

Calls one of the 3 sub-function depending on what type of transfer this QH
is for.  Also adds some printing.

.. _`dwc2_uframe_unschedule`:

dwc2_uframe_unschedule
======================

.. c:function:: void dwc2_uframe_unschedule(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Undoes \ :c:func:`dwc2_uframe_schedule`\ .

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

.. _`dwc2_pick_first_frame`:

dwc2_pick_first_frame
=====================

.. c:function:: void dwc2_pick_first_frame(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Choose 1st frame for qh that's already scheduled

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        QH for a periodic endpoint

.. _`dwc2_pick_first_frame.description`:

Description
-----------

Takes a qh that has already been scheduled (which means we know we have the
bandwdith reserved for us) and set the next_active_frame and the
start_active_frame.

This is expected to be called on qh's that weren't previously actively
running.  It just picks the next frame that we can fit into without any
thought about the past.

.. _`dwc2_do_reserve`:

dwc2_do_reserve
===============

.. c:function:: int dwc2_do_reserve(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Make a periodic reservation

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

.. _`dwc2_do_reserve.description`:

Description
-----------

Try to allocate space in the periodic schedule.  Depending on parameters
this might use the microframe scheduler or the dumb scheduler.

.. _`dwc2_do_reserve.return`:

Return
------

0 upon success; error upon failure.

.. _`dwc2_do_unreserve`:

dwc2_do_unreserve
=================

.. c:function:: void dwc2_do_unreserve(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Actually release the periodic reservation

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

.. _`dwc2_do_unreserve.description`:

Description
-----------

This function actually releases the periodic bandwidth that was reserved
by the given qh.

.. _`dwc2_unreserve_timer_fn`:

dwc2_unreserve_timer_fn
=======================

.. c:function:: void dwc2_unreserve_timer_fn(struct timer_list *t)

    Timer function to release periodic reservation

    :param struct timer_list \*t:
        *undescribed*

.. _`dwc2_unreserve_timer_fn.description`:

Description
-----------

According to the kernel doc for \ :c:func:`usb_submit_urb`\  (specifically the part about
"Reserved Bandwidth Transfers"), we need to keep a reservation active as
long as a device driver keeps submitting.  Since we're using HCD_BH to give
back the URB we need to give the driver a little bit of time before we
release the reservation.  This worker is called after the appropriate
delay.

.. _`dwc2_check_max_xfer_size`:

dwc2_check_max_xfer_size
========================

.. c:function:: int dwc2_check_max_xfer_size(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Checks that the max transfer size allowed in a host channel is large enough to handle the maximum data transfer in a single (micro)frame for a periodic transfer

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        QH for a periodic endpoint

.. _`dwc2_check_max_xfer_size.return`:

Return
------

0 if successful, negative error code otherwise

.. _`dwc2_schedule_periodic`:

dwc2_schedule_periodic
======================

.. c:function:: int dwc2_schedule_periodic(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Schedules an interrupt or isochronous transfer in the periodic schedule

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer. The QH should already contain the
        scheduling information.

.. _`dwc2_schedule_periodic.return`:

Return
------

0 if successful, negative error code otherwise

.. _`dwc2_deschedule_periodic`:

dwc2_deschedule_periodic
========================

.. c:function:: void dwc2_deschedule_periodic(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Removes an interrupt or isochronous transfer from the periodic schedule

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer

.. _`dwc2_qh_init`:

dwc2_qh_init
============

.. c:function:: void dwc2_qh_init(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh, struct dwc2_hcd_urb *urb, gfp_t mem_flags)

    Initializes a QH structure

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        The QH to init

    :param struct dwc2_hcd_urb \*urb:
        Holds the information about the device/endpoint needed to initialize
        the QH

    :param gfp_t mem_flags:
        Flags for allocating memory.

.. _`dwc2_hcd_qh_create`:

dwc2_hcd_qh_create
==================

.. c:function:: struct dwc2_qh *dwc2_hcd_qh_create(struct dwc2_hsotg *hsotg, struct dwc2_hcd_urb *urb, gfp_t mem_flags)

    Allocates and initializes a QH

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_hcd_urb \*urb:
        Holds the information about the device/endpoint needed
        to initialize the QH

    :param gfp_t mem_flags:
        *undescribed*

.. _`dwc2_hcd_qh_create.return`:

Return
------

Pointer to the newly allocated QH, or NULL on error

.. _`dwc2_hcd_qh_free`:

dwc2_hcd_qh_free
================

.. c:function:: void dwc2_hcd_qh_free(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Frees the QH

    :param struct dwc2_hsotg \*hsotg:
        HCD instance

    :param struct dwc2_qh \*qh:
        The QH to free

.. _`dwc2_hcd_qh_free.description`:

Description
-----------

QH should already be removed from the list. QTD list should already be empty
if called from URB Dequeue.

Must NOT be called with interrupt disabled or spinlock held

.. _`dwc2_hcd_qh_add`:

dwc2_hcd_qh_add
===============

.. c:function:: int dwc2_hcd_qh_add(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Adds a QH to either the non periodic or periodic schedule if it is not already in the schedule. If the QH is already in the schedule, no action is taken.

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        The QH to add

.. _`dwc2_hcd_qh_add.return`:

Return
------

0 if successful, negative error code otherwise

.. _`dwc2_hcd_qh_unlink`:

dwc2_hcd_qh_unlink
==================

.. c:function:: void dwc2_hcd_qh_unlink(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Removes a QH from either the non-periodic or periodic schedule. Memory is not freed.

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure

    :param struct dwc2_qh \*qh:
        QH to remove from schedule

.. _`dwc2_next_for_periodic_split`:

dwc2_next_for_periodic_split
============================

.. c:function:: int dwc2_next_for_periodic_split(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh, u16 frame_number)

    Set next_active_frame midway thru a split.

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

    :param u16 frame_number:
        The current frame number.

.. _`dwc2_next_for_periodic_split.description`:

Description
-----------

This is called for setting next_active_frame for periodic splits for all but
the first packet of the split.  Confusing?  I thought so...

Periodic splits are single low/full speed transfers that we end up splitting
up into several high speed transfers.  They always fit into one full (1 ms)
frame but might be split over several microframes (125 us each).  We to put
each of the parts on a very specific high speed frame.

This function figures out where the next active uFrame needs to be.

.. _`dwc2_next_for_periodic_split.return`:

Return
------

number missed by (or 0 if we didn't miss).

.. _`dwc2_next_periodic_start`:

dwc2_next_periodic_start
========================

.. c:function:: int dwc2_next_periodic_start(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh, u16 frame_number)

    Set next_active_frame for next transfer start

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure

    :param struct dwc2_qh \*qh:
        QH for the periodic transfer.

    :param u16 frame_number:
        The current frame number.

.. _`dwc2_next_periodic_start.description`:

Description
-----------

This is called for setting next_active_frame for a periodic transfer for
all cases other than midway through a periodic split.  This will also update
start_active_frame.

Since we \_always\_ keep start_active_frame as the start of the previous

.. _`dwc2_next_periodic_start.transfer-this-is-normally-pretty-easy`:

transfer this is normally pretty easy
-------------------------------------

we just add our interval to
start_active_frame and we've got our answer.

The tricks come into play if we miss.  In that case we'll look for the next
slot we can fit into.

.. _`dwc2_next_periodic_start.return`:

Return
------

number missed by (or 0 if we didn't miss).

.. _`dwc2_hcd_qtd_init`:

dwc2_hcd_qtd_init
=================

.. c:function:: void dwc2_hcd_qtd_init(struct dwc2_qtd *qtd, struct dwc2_hcd_urb *urb)

    Initializes a QTD structure

    :param struct dwc2_qtd \*qtd:
        The QTD to initialize

    :param struct dwc2_hcd_urb \*urb:
        The associated URB

.. _`dwc2_hcd_qtd_add`:

dwc2_hcd_qtd_add
================

.. c:function:: int dwc2_hcd_qtd_add(struct dwc2_hsotg *hsotg, struct dwc2_qtd *qtd, struct dwc2_qh *qh)

    Adds a QTD to the QTD-list of a QH Caller must hold driver lock.

    :param struct dwc2_hsotg \*hsotg:
        The DWC HCD structure

    :param struct dwc2_qtd \*qtd:
        The QTD to add

    :param struct dwc2_qh \*qh:
        Queue head to add qtd to

.. _`dwc2_hcd_qtd_add.return`:

Return
------

0 if successful, negative error code otherwise

If the QH to which the QTD is added is not currently scheduled, it is placed
into the proper schedule based on its EP type.

.. This file was automatic generated / don't edit.

