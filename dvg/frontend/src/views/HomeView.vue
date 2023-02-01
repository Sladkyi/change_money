<template>
    <HeaderView />
    <ContentView />
    <FooterView />
    <ContinueView />
</template>

<script>
import ContentView from '@/components/content.vue'
import FooterView from '@/components/footer.vue'
import HeaderView from '@/components/header.vue'
import ContinueView from '@/components/continue.vue'

export default {
  name: 'HomeView',
  components: {
    HeaderView,
    ContentView,
    FooterView,
    ContinueView,
  }
}
</script>

