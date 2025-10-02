<script lang="ts" setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { Message } from '@arco-design/web-vue'
import { debugApp } from '@/services/app.ts'

const query = ref('')
const messages = ref<any[]>([])
const isLoading = ref(false)
const route = useRoute()

const clearMessages = () => {
  messages.value = []
}

const send = async () => {
  if (!query.value) {
    Message.error('用户提问不能为空')
    return
  }
  if (isLoading.value) {
    Message.warning('上一次回复还未结束，请稍等')
    return
  }

  try {
    const humanQuery = query.value
    messages.value.push({
      role: 'human',
      content: humanQuery,
    })
    query.value = ''
    isLoading.value = true

    const response = await debugApp(route.params.app_id as string, humanQuery)
    const content = response.data.content

    messages.value.push({
      role: 'ai',
      content: content,
    })
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <!--最外层容器。高度撑满整个屏幕 -->
  <div class="min-h-screen">
    <!--顶部导航 -->
    <header class="flex items-center h-[74px] bg-gray-100 border-b border-gray-200 px-4">
      顶部导航
    </header>
    <!--底部内容区 -->
    <div class="flex flex-row h-[cal(100vh-74px)]">
      <div class="w-2/3 bg-gray-50 h-full">
        <header class="flex items-center h-16 border-b border-gray-200 px-7 text-xl text-gray-700">
          应用编排
        </header>
        <div class="flex flex-row h=[cal(100% - 64px)]">
          <div class="flex-1 border-r border-gray-200 p-6">人设与逻辑回复</div>
          <div class="flex-1 p-6">应用能力</div>
        </div>
      </div>
      <div class="w-1/3 flex flex-col bg-white h-full">
        <header
          class="flex flex-shrink-0 items-center h-16 px-4 text-xl bg-white border-b border-gray-200 shadow-sm"
        >
          调试与预览
        </header>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
