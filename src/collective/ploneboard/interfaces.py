# -*- coding: UTF-8 -*-
from plone.app.textfield import RichText
from plone.directives import form
from zope import schema
from collective.ploneboard import _
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


class IMessageboard(form.Schema):
	category=schema.Text(
		title=_(u"Categories"),
        description=_(u"Seperate by writing in different lines"),
		required=False
		)


class ITopic(form.Schema):
    """categories = SimpleVocabulary(
    [SimpleTerm(value=u'tag1', title=_(u'Tag1')),
     SimpleTerm(value=u'tag2', title=_(u'Tag2')),
     SimpleTerm(value=u'tag3', title=_(u'Tag3'))]
    )
    """
    
    category = schema.Choice(
            title=_(u"Category"),
            description=_(u"Choose to tag your Topic"),
            values= ["A","B"],
            required=False,
        )

class IConversation(form.Schema):
    """
    """

    text = RichText(
        title=_(u"Text"),
        required=True
    )
