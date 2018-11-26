.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas/mesh.c

.. _`lbs_anycast_get`:

lbs_anycast_get
===============

.. c:function:: ssize_t lbs_anycast_get(struct device *dev, struct device_attribute *attr, char *buf)

    Get function for sysfs attribute anycast_mask

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer where data will be returned
    :type buf: char \*

.. _`lbs_anycast_set`:

lbs_anycast_set
===============

.. c:function:: ssize_t lbs_anycast_set(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set function for sysfs attribute anycast_mask

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer that contains new attribute value
    :type buf: const char \*

    :param count:
        size of buffer
    :type count: size_t

.. _`lbs_prb_rsp_limit_get`:

lbs_prb_rsp_limit_get
=====================

.. c:function:: ssize_t lbs_prb_rsp_limit_get(struct device *dev, struct device_attribute *attr, char *buf)

    Get function for sysfs attribute prb_rsp_limit

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer where data will be returned
    :type buf: char \*

.. _`lbs_prb_rsp_limit_set`:

lbs_prb_rsp_limit_set
=====================

.. c:function:: ssize_t lbs_prb_rsp_limit_set(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set function for sysfs attribute prb_rsp_limit

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer that contains new attribute value
    :type buf: const char \*

    :param count:
        size of buffer
    :type count: size_t

.. _`lbs_mesh_get`:

lbs_mesh_get
============

.. c:function:: ssize_t lbs_mesh_get(struct device *dev, struct device_attribute *attr, char *buf)

    Get function for sysfs attribute mesh

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer where data will be returned
    :type buf: char \*

.. _`lbs_mesh_set`:

lbs_mesh_set
============

.. c:function:: ssize_t lbs_mesh_set(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set function for sysfs attribute mesh

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer that contains new attribute value
    :type buf: const char \*

    :param count:
        size of buffer
    :type count: size_t

.. _`bootflag_get`:

bootflag_get
============

.. c:function:: ssize_t bootflag_get(struct device *dev, struct device_attribute *attr, char *buf)

    Get function for sysfs attribute bootflag

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer where data will be returned
    :type buf: char \*

.. _`bootflag_set`:

bootflag_set
============

.. c:function:: ssize_t bootflag_set(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set function for sysfs attribute bootflag

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer that contains new attribute value
    :type buf: const char \*

    :param count:
        size of buffer
    :type count: size_t

.. _`boottime_get`:

boottime_get
============

.. c:function:: ssize_t boottime_get(struct device *dev, struct device_attribute *attr, char *buf)

    Get function for sysfs attribute boottime

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer where data will be returned
    :type buf: char \*

.. _`boottime_set`:

boottime_set
============

.. c:function:: ssize_t boottime_set(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set function for sysfs attribute boottime

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer that contains new attribute value
    :type buf: const char \*

    :param count:
        size of buffer
    :type count: size_t

.. _`channel_get`:

channel_get
===========

.. c:function:: ssize_t channel_get(struct device *dev, struct device_attribute *attr, char *buf)

    Get function for sysfs attribute channel

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer where data will be returned
    :type buf: char \*

.. _`channel_set`:

channel_set
===========

.. c:function:: ssize_t channel_set(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set function for sysfs attribute channel

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer that contains new attribute value
    :type buf: const char \*

    :param count:
        size of buffer
    :type count: size_t

.. _`mesh_id_get`:

mesh_id_get
===========

.. c:function:: ssize_t mesh_id_get(struct device *dev, struct device_attribute *attr, char *buf)

    Get function for sysfs attribute mesh_id

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer where data will be returned
    :type buf: char \*

.. _`mesh_id_set`:

mesh_id_set
===========

.. c:function:: ssize_t mesh_id_set(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set function for sysfs attribute mesh_id

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer that contains new attribute value
    :type buf: const char \*

    :param count:
        size of buffer
    :type count: size_t

.. _`protocol_id_get`:

protocol_id_get
===============

.. c:function:: ssize_t protocol_id_get(struct device *dev, struct device_attribute *attr, char *buf)

    Get function for sysfs attribute protocol_id

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer where data will be returned
    :type buf: char \*

.. _`protocol_id_set`:

protocol_id_set
===============

.. c:function:: ssize_t protocol_id_set(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set function for sysfs attribute protocol_id

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer that contains new attribute value
    :type buf: const char \*

    :param count:
        size of buffer
    :type count: size_t

.. _`metric_id_get`:

metric_id_get
=============

.. c:function:: ssize_t metric_id_get(struct device *dev, struct device_attribute *attr, char *buf)

    Get function for sysfs attribute metric_id

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer where data will be returned
    :type buf: char \*

.. _`metric_id_set`:

metric_id_set
=============

.. c:function:: ssize_t metric_id_set(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set function for sysfs attribute metric_id

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer that contains new attribute value
    :type buf: const char \*

    :param count:
        size of buffer
    :type count: size_t

.. _`capability_get`:

capability_get
==============

.. c:function:: ssize_t capability_get(struct device *dev, struct device_attribute *attr, char *buf)

    Get function for sysfs attribute capability

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer where data will be returned
    :type buf: char \*

.. _`capability_set`:

capability_set
==============

.. c:function:: ssize_t capability_set(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set function for sysfs attribute capability

    :param dev:
        the \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param attr:
        device attributes
    :type attr: struct device_attribute \*

    :param buf:
        buffer that contains new attribute value
    :type buf: const char \*

    :param count:
        size of buffer
    :type count: size_t

.. _`lbs_mesh_stop`:

lbs_mesh_stop
=============

.. c:function:: int lbs_mesh_stop(struct net_device *dev)

    close the mshX interface

    :param dev:
        A pointer to \ :c:type:`struct net_device <net_device>`\  structure
    :type dev: struct net_device \*

.. _`lbs_mesh_stop.return`:

Return
------

0

.. _`lbs_mesh_dev_open`:

lbs_mesh_dev_open
=================

.. c:function:: int lbs_mesh_dev_open(struct net_device *dev)

    open the mshX interface

    :param dev:
        A pointer to \ :c:type:`struct net_device <net_device>`\  structure
    :type dev: struct net_device \*

.. _`lbs_mesh_dev_open.return`:

Return
------

0 or -EBUSY if monitor mode active

.. _`lbs_add_mesh`:

lbs_add_mesh
============

.. c:function:: int lbs_add_mesh(struct lbs_private *priv)

    add mshX interface

    :param priv:
        A pointer to the \ :c:type:`struct lbs_private <lbs_private>`\  structure
    :type priv: struct lbs_private \*

.. _`lbs_add_mesh.return`:

Return
------

0 if successful, -X otherwise

.. This file was automatic generated / don't edit.

