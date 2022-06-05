<template>
  <div class="dashboard-container">
    <div class="dashboard-text">欢迎: {{ name }}</div>
    <div class="dashboard-backgroud">
      <img src="../../assets/bk01.png">
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
.dashboard-text {
    margin: 0;
    margin: 0;
    font-family: 'Times New Roman', Times, serif;
    color: #070707;
    text-align: center;
}
.dashboard-backgroud {
  text-align: center;
}
</style>
