.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/init.c

.. _`mei_fw_status2str`:

mei_fw_status2str
=================

.. c:function:: ssize_t mei_fw_status2str(struct mei_fw_status *fw_status, char *buf, size_t len)

    convert fw status registers to printable string

    :param struct mei_fw_status \*fw_status:
        firmware status

    :param char \*buf:
        string buffer at minimal size MEI_FW_STATUS_STR_SZ

    :param size_t len:
        buffer len must be >= MEI_FW_STATUS_STR_SZ

.. _`mei_fw_status2str.return`:

Return
------

number of bytes written or -EINVAL if buffer is to small

.. _`mei_cancel_work`:

mei_cancel_work
===============

.. c:function:: void mei_cancel_work(struct mei_device *dev)

    Cancel mei background jobs

    :param struct mei_device \*dev:
        the device structure

.. _`mei_reset`:

mei_reset
=========

.. c:function:: int mei_reset(struct mei_device *dev)

    resets host and fw.

    :param struct mei_device \*dev:
        the device structure

.. _`mei_reset.return`:

Return
------

0 on success or < 0 if the reset hasn't succeeded

.. _`mei_start`:

mei_start
=========

.. c:function:: int mei_start(struct mei_device *dev)

    initializes host and fw to start work.

    :param struct mei_device \*dev:
        the device structure

.. _`mei_start.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_restart`:

mei_restart
===========

.. c:function:: int mei_restart(struct mei_device *dev)

    restart device after suspend

    :param struct mei_device \*dev:
        the device structure

.. _`mei_restart.return`:

Return
------

0 on success or -ENODEV if the restart hasn't succeeded

.. _`mei_write_is_idle`:

mei_write_is_idle
=================

.. c:function:: bool mei_write_is_idle(struct mei_device *dev)

    check if the write queues are idle

    :param struct mei_device \*dev:
        the device structure

.. _`mei_write_is_idle.return`:

Return
------

true of there is no pending write

.. _`mei_device_init`:

mei_device_init
===============

.. c:function:: void mei_device_init(struct mei_device *dev, struct device *device, const struct mei_hw_ops *hw_ops)

    - initialize mei_device structure

    :param struct mei_device \*dev:
        the mei device

    :param struct device \*device:
        the device structure

    :param const struct mei_hw_ops \*hw_ops:
        hw operations

.. This file was automatic generated / don't edit.

