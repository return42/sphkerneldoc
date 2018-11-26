.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_mode_object.c

.. _`drm_mode_object_add`:

drm_mode_object_add
===================

.. c:function:: int drm_mode_object_add(struct drm_device *dev, struct drm_mode_object *obj, uint32_t obj_type)

    allocate a new modeset identifier

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param obj:
        object pointer, used to generate unique ID
    :type obj: struct drm_mode_object \*

    :param obj_type:
        object type
    :type obj_type: uint32_t

.. _`drm_mode_object_add.description`:

Description
-----------

Create a unique identifier based on \ ``ptr``\  in \ ``dev``\ 's identifier space.  Used
for tracking modes, CRTCs and connectors.

.. _`drm_mode_object_add.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_mode_object_unregister`:

drm_mode_object_unregister
==========================

.. c:function:: void drm_mode_object_unregister(struct drm_device *dev, struct drm_mode_object *object)

    free a modeset identifer

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param object:
        object to free
    :type object: struct drm_mode_object \*

.. _`drm_mode_object_unregister.description`:

Description
-----------

Free \ ``id``\  from \ ``dev``\ 's unique identifier pool.
This function can be called multiple times, and guards against
multiple removals.
These modeset identifiers are _not_ reference counted. Hence don't use this
for reference counted modeset objects like framebuffers.

.. _`drm_mode_object_lease_required`:

drm_mode_object_lease_required
==============================

.. c:function:: bool drm_mode_object_lease_required(uint32_t type)

    check types which must be leased to be used

    :param type:
        type of object
    :type type: uint32_t

.. _`drm_mode_object_lease_required.description`:

Description
-----------

Returns whether the provided type of drm_mode_object must
be owned or leased to be used by a process.

.. _`drm_mode_object_find`:

drm_mode_object_find
====================

.. c:function:: struct drm_mode_object *drm_mode_object_find(struct drm_device *dev, struct drm_file *file_priv, uint32_t id, uint32_t type)

    look up a drm object with static lifetime

    :param dev:
        drm device
    :type dev: struct drm_device \*

    :param file_priv:
        drm file
    :type file_priv: struct drm_file \*

    :param id:
        id of the mode object
    :type id: uint32_t

    :param type:
        type of the mode object
    :type type: uint32_t

.. _`drm_mode_object_find.description`:

Description
-----------

This function is used to look up a modeset object. It will acquire a
reference for reference counted objects. This reference must be dropped again
by callind \ :c:func:`drm_mode_object_put`\ .

.. _`drm_mode_object_put`:

drm_mode_object_put
===================

.. c:function:: void drm_mode_object_put(struct drm_mode_object *obj)

    release a mode object reference

    :param obj:
        DRM mode object
    :type obj: struct drm_mode_object \*

.. _`drm_mode_object_put.description`:

Description
-----------

This function decrements the object's refcount if it is a refcounted modeset
object. It is a no-op on any other object. This is used to drop references
acquired with \ :c:func:`drm_mode_object_get`\ .

.. _`drm_mode_object_get`:

drm_mode_object_get
===================

.. c:function:: void drm_mode_object_get(struct drm_mode_object *obj)

    acquire a mode object reference

    :param obj:
        DRM mode object
    :type obj: struct drm_mode_object \*

.. _`drm_mode_object_get.description`:

Description
-----------

This function increments the object's refcount if it is a refcounted modeset
object. It is a no-op on any other object. References should be dropped again
by calling \ :c:func:`drm_mode_object_put`\ .

.. _`drm_object_attach_property`:

drm_object_attach_property
==========================

.. c:function:: void drm_object_attach_property(struct drm_mode_object *obj, struct drm_property *property, uint64_t init_val)

    attach a property to a modeset object

    :param obj:
        drm modeset object
    :type obj: struct drm_mode_object \*

    :param property:
        property to attach
    :type property: struct drm_property \*

    :param init_val:
        initial value of the property
    :type init_val: uint64_t

.. _`drm_object_attach_property.description`:

Description
-----------

This attaches the given property to the modeset object with the given initial
value. Currently this function cannot fail since the properties are stored in
a statically sized array.

.. _`drm_object_property_set_value`:

drm_object_property_set_value
=============================

.. c:function:: int drm_object_property_set_value(struct drm_mode_object *obj, struct drm_property *property, uint64_t val)

    set the value of a property

    :param obj:
        drm mode object to set property value for
    :type obj: struct drm_mode_object \*

    :param property:
        property to set
    :type property: struct drm_property \*

    :param val:
        value the property should be set to
    :type val: uint64_t

.. _`drm_object_property_set_value.description`:

Description
-----------

This function sets a given property on a given object. This function only
changes the software state of the property, it does not call into the
driver's ->set_property callback.

Note that atomic drivers should not have any need to call this, the core will
ensure consistency of values reported back to userspace through the
appropriate ->atomic_get_property callback. Only legacy drivers should call
this function to update the tracked value (after clamping and other
restrictions have been applied).

.. _`drm_object_property_set_value.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_object_property_get_value`:

drm_object_property_get_value
=============================

.. c:function:: int drm_object_property_get_value(struct drm_mode_object *obj, struct drm_property *property, uint64_t *val)

    retrieve the value of a property

    :param obj:
        drm mode object to get property value from
    :type obj: struct drm_mode_object \*

    :param property:
        property to retrieve
    :type property: struct drm_property \*

    :param val:
        storage for the property value
    :type val: uint64_t \*

.. _`drm_object_property_get_value.description`:

Description
-----------

This function retrieves the softare state of the given property for the given
property. Since there is no driver callback to retrieve the current property
value this might be out of sync with the hardware, depending upon the driver
and property.

Atomic drivers should never call this function directly, the core will read
out property values through the various ->atomic_get_property callbacks.

.. _`drm_object_property_get_value.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_mode_obj_get_properties_ioctl`:

drm_mode_obj_get_properties_ioctl
=================================

.. c:function:: int drm_mode_obj_get_properties_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get the current value of a object's property

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param data:
        ioctl data
    :type data: void \*

    :param file_priv:
        DRM file info
    :type file_priv: struct drm_file \*

.. _`drm_mode_obj_get_properties_ioctl.description`:

Description
-----------

This function retrieves the current value for an object's property. Compared
to the connector specific ioctl this one is extended to also work on crtc and
plane objects.

Called by the user via ioctl.

.. _`drm_mode_obj_get_properties_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

