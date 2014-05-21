from zope.component import getMultiAdapter

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class MessageboardView(BrowserView):

    template = ViewPageTemplateFile('messageboard.pt')

    def __call__(self):
	context = self.context.aq_inner
	#print context.category
	context.cats = context.category.split('\r\n')
	#print context.cats
        return self.template()

    def topics(self):
        topics = []
        for topic_id in self.context.objectIds():
            topic = self.context[topic_id]
            conversations = getMultiAdapter(
                (topic, self.request),
                name="view"
            ).conversations()
            topics.append({
                'title': topic.title,
		'category': topic.category,
                'url': topic.absolute_url(),
                'conversations': conversations,
            })
        return topics
