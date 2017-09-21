.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/ctl.h

.. _`tb_cfg_request`:

struct tb_cfg_request
=====================

.. c:type:: struct tb_cfg_request

    Control channel request

.. _`tb_cfg_request.definition`:

Definition
----------

.. code-block:: c

    struct tb_cfg_request {
        struct kref kref;
        struct tb_ctl *ctl;
        const void *request;
        size_t request_size;
        enum tb_cfg_pkg_type request_type;
        void *response;
        size_t response_size;
        enum tb_cfg_pkg_type response_type;
        size_t npackets;
        bool (*match)(const struct tb_cfg_request *req, const struct ctl_pkg *pkg);
        bool (*copy)(struct tb_cfg_request *req, const struct ctl_pkg *pkg);
        void (*callback)(void *callback_data);
        void *callback_data;
        unsigned long flags;
        struct work_struct work;
        struct tb_cfg_result result;
        struct list_head list;
    }

.. _`tb_cfg_request.members`:

Members
-------

kref
    Reference count

ctl
    Pointer to the control channel structure. Only set when the
    request is queued.

request
    *undescribed*

request_size
    Size of the request packet (in bytes)

request_type
    Type of the request packet

response
    Response is stored here

response_size
    Maximum size of one response packet

response_type
    Expected type of the response packet

npackets
    Number of packets expected to be returned with this request

match
    Function used to match the incoming packet

copy
    Function used to copy the incoming packet to \ ``response``\ 

callback
    Callback called when the request is finished successfully

callback_data
    Data to be passed to \ ``callback``\ 

flags
    Flags for the request

work
    Work item used to complete the request

result
    Result after the request has been completed

list
    Requests are queued using this field

.. _`tb_cfg_request.description`:

Description
-----------

An arbitrary request over Thunderbolt control channel. For standard
control channel message, one should use tb_cfg_read/write() and
friends if possible.

.. This file was automatic generated / don't edit.

