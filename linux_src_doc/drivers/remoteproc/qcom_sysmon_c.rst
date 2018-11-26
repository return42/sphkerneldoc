.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/qcom_sysmon.c

.. _`sysmon_send_event`:

sysmon_send_event
=================

.. c:function:: void sysmon_send_event(struct qcom_sysmon *sysmon, const char *name)

    send notification of other remote's SSR event

    :param sysmon:
        sysmon context
    :type sysmon: struct qcom_sysmon \*

    :param name:
        other remote's name
    :type name: const char \*

.. _`sysmon_request_shutdown`:

sysmon_request_shutdown
=======================

.. c:function:: void sysmon_request_shutdown(struct qcom_sysmon *sysmon)

    request graceful shutdown of remote

    :param sysmon:
        sysmon context
    :type sysmon: struct qcom_sysmon \*

.. _`ssctl_request_shutdown`:

ssctl_request_shutdown
======================

.. c:function:: void ssctl_request_shutdown(struct qcom_sysmon *sysmon)

    request shutdown via SSCTL QMI service

    :param sysmon:
        sysmon context
    :type sysmon: struct qcom_sysmon \*

.. _`ssctl_send_event`:

ssctl_send_event
================

.. c:function:: void ssctl_send_event(struct qcom_sysmon *sysmon, const char *name)

    send notification of other remote's SSR event

    :param sysmon:
        sysmon context
    :type sysmon: struct qcom_sysmon \*

    :param name:
        other remote's name
    :type name: const char \*

.. _`ssctl_new_server`:

ssctl_new_server
================

.. c:function:: int ssctl_new_server(struct qmi_handle *qmi, struct qmi_service *svc)

    QMI callback indicating a new service

    :param qmi:
        QMI handle
    :type qmi: struct qmi_handle \*

    :param svc:
        service information
    :type svc: struct qmi_service \*

.. _`ssctl_new_server.return`:

Return
------

0 if we're interested in this service, -EINVAL otherwise.

.. _`ssctl_del_server`:

ssctl_del_server
================

.. c:function:: void ssctl_del_server(struct qmi_handle *qmi, struct qmi_service *svc)

    QMI callback indicating that \ ``svc``\  is removed

    :param qmi:
        QMI handle
    :type qmi: struct qmi_handle \*

    :param svc:
        service information
    :type svc: struct qmi_service \*

.. _`sysmon_notify`:

sysmon_notify
=============

.. c:function:: int sysmon_notify(struct notifier_block *nb, unsigned long event, void *data)

    notify sysmon target of another's SSR

    :param nb:
        notifier_block associated with sysmon instance
    :type nb: struct notifier_block \*

    :param event:
        unused
    :type event: unsigned long

    :param data:
        SSR identifier of the remote that is going down
    :type data: void \*

.. _`qcom_add_sysmon_subdev`:

qcom_add_sysmon_subdev
======================

.. c:function:: struct qcom_sysmon *qcom_add_sysmon_subdev(struct rproc *rproc, const char *name, int ssctl_instance)

    create a sysmon subdev for the given remoteproc

    :param rproc:
        rproc context to associate the subdev with
    :type rproc: struct rproc \*

    :param name:
        name of this subdev, to use in SSR
    :type name: const char \*

    :param ssctl_instance:
        instance id of the ssctl QMI service
    :type ssctl_instance: int

.. _`qcom_add_sysmon_subdev.return`:

Return
------

A new qcom_sysmon object, or NULL on failure

.. _`qcom_remove_sysmon_subdev`:

qcom_remove_sysmon_subdev
=========================

.. c:function:: void qcom_remove_sysmon_subdev(struct qcom_sysmon *sysmon)

    release a qcom_sysmon

    :param sysmon:
        sysmon context, as retrieved by \ :c:func:`qcom_add_sysmon_subdev`\ 
    :type sysmon: struct qcom_sysmon \*

.. _`sysmon_probe`:

sysmon_probe
============

.. c:function:: int sysmon_probe(struct rpmsg_device *rpdev)

    probe sys_mon channel

    :param rpdev:
        rpmsg device handle
    :type rpdev: struct rpmsg_device \*

.. _`sysmon_probe.description`:

Description
-----------

Find the sysmon context associated with the ancestor remoteproc and assign
this rpmsg device with said sysmon context.

.. _`sysmon_probe.return`:

Return
------

0 on success, negative errno on failure.

.. _`sysmon_remove`:

sysmon_remove
=============

.. c:function:: void sysmon_remove(struct rpmsg_device *rpdev)

    sys_mon channel remove handler

    :param rpdev:
        rpmsg device handle
    :type rpdev: struct rpmsg_device \*

.. _`sysmon_remove.description`:

Description
-----------

Disassociate the rpmsg device with the sysmon instance.

.. This file was automatic generated / don't edit.

