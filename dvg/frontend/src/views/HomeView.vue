<template>
    <ContentView />
    <FooterView />
    <HeaderView />
</template>

<script>
import ContentView from '@/components/content.vue'
import FooterView from '@/components/footer.vue'
import HeaderView from '@/components/header.vue'

export default {
  name: 'HomeView',
  components: {
    HeaderView,
    ContentView,
    FooterView,
  }
}

</script>

