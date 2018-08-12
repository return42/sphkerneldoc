.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/qcom_sysmon.c

.. _`sysmon_send_event`:

sysmon_send_event
=================

.. c:function:: void sysmon_send_event(struct qcom_sysmon *sysmon, const char *name)

    send notification of other remote's SSR event

    :param struct qcom_sysmon \*sysmon:
        sysmon context

    :param const char \*name:
        other remote's name

.. _`sysmon_request_shutdown`:

sysmon_request_shutdown
=======================

.. c:function:: void sysmon_request_shutdown(struct qcom_sysmon *sysmon)

    request graceful shutdown of remote

    :param struct qcom_sysmon \*sysmon:
        sysmon context

.. _`ssctl_request_shutdown`:

ssctl_request_shutdown
======================

.. c:function:: void ssctl_request_shutdown(struct qcom_sysmon *sysmon)

    request shutdown via SSCTL QMI service

    :param struct qcom_sysmon \*sysmon:
        sysmon context

.. _`ssctl_send_event`:

ssctl_send_event
================

.. c:function:: void ssctl_send_event(struct qcom_sysmon *sysmon, const char *name)

    send notification of other remote's SSR event

    :param struct qcom_sysmon \*sysmon:
        sysmon context

    :param const char \*name:
        other remote's name

.. _`ssctl_new_server`:

ssctl_new_server
================

.. c:function:: int ssctl_new_server(struct qmi_handle *qmi, struct qmi_service *svc)

    QMI callback indicating a new service

    :param struct qmi_handle \*qmi:
        QMI handle

    :param struct qmi_service \*svc:
        service information

.. _`ssctl_new_server.return`:

Return
------

0 if we're interested in this service, -EINVAL otherwise.

.. _`ssctl_del_server`:

ssctl_del_server
================

.. c:function:: void ssctl_del_server(struct qmi_handle *qmi, struct qmi_service *svc)

    QMI callback indicating that \ ``svc``\  is removed

    :param struct qmi_handle \*qmi:
        QMI handle

    :param struct qmi_service \*svc:
        service information

.. _`sysmon_notify`:

sysmon_notify
=============

.. c:function:: int sysmon_notify(struct notifier_block *nb, unsigned long event, void *data)

    notify sysmon target of another's SSR

    :param struct notifier_block \*nb:
        notifier_block associated with sysmon instance

    :param unsigned long event:
        unused

    :param void \*data:
        SSR identifier of the remote that is going down

.. _`qcom_add_sysmon_subdev`:

qcom_add_sysmon_subdev
======================

.. c:function:: struct qcom_sysmon *qcom_add_sysmon_subdev(struct rproc *rproc, const char *name, int ssctl_instance)

    create a sysmon subdev for the given remoteproc

    :param struct rproc \*rproc:
        rproc context to associate the subdev with

    :param const char \*name:
        name of this subdev, to use in SSR

    :param int ssctl_instance:
        instance id of the ssctl QMI service

.. _`qcom_add_sysmon_subdev.return`:

Return
------

A new qcom_sysmon object, or NULL on failure

.. _`qcom_remove_sysmon_subdev`:

qcom_remove_sysmon_subdev
=========================

.. c:function:: void qcom_remove_sysmon_subdev(struct qcom_sysmon *sysmon)

    release a qcom_sysmon

    :param struct qcom_sysmon \*sysmon:
        sysmon context, as retrieved by \ :c:func:`qcom_add_sysmon_subdev`\ 

.. _`sysmon_probe`:

sysmon_probe
============

.. c:function:: int sysmon_probe(struct rpmsg_device *rpdev)

    probe sys_mon channel

    :param struct rpmsg_device \*rpdev:
        rpmsg device handle

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

    :param struct rpmsg_device \*rpdev:
        rpmsg device handle

.. _`sysmon_remove.description`:

Description
-----------

Disassociate the rpmsg device with the sysmon instance.

.. This file was automatic generated / don't edit.

