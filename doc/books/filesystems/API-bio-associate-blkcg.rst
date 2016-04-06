
.. _API-bio-associate-blkcg:

===================
bio_associate_blkcg
===================

*man bio_associate_blkcg(9)*

*4.6.0-rc1*

associate a bio with the specified blkcg


Synopsis
========

.. c:function:: int bio_associate_blkcg( struct bio * bio, struct cgroup_subsys_state * blkcg_css )

Arguments
=========

``bio``
    target bio

``blkcg_css``
    css of the blkcg to associate


Description
===========

Associate ``bio`` with the blkcg specified by ``blkcg_css``. Block layer will treat ``bio`` as if it were issued by a task which belongs to the blkcg.

This function takes an extra reference of ``blkcg_css`` which will be put when ``bio`` is released. The caller must own ``bio`` and is responsible for synchronizing calls to this
function.
