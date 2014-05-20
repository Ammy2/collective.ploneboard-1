# -*- coding: UTF-8 -*-
from plone.app.textfield import RichText
from plone.directives import form
from zope import schema
from collective.ploneboard import _


class IMessageboard(form.Schema):
	category=schema.Text(
		title=_(u"Categories"),
		required=False
		)


class ITopic(form.Schema):
    """
    """


class IConversation(form.Schema):
    """
    """

    text = RichText(
        title=_(u"Text"),
        required=True
    )
