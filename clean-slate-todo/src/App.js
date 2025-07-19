import React, { useState } from 'react';
import { Plus, X, Check, Tag, Edit3, Save } from 'lucide-react';

export default function MinimalistTodo() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');
  const [newTag, setNewTag] = useState('');
  const [filterTag, setFilterTag] = useState('');
  const [customTags, setCustomTags] = useState([]);
  const [editingTag, setEditingTag] = useState(null);
  const [editTagValue, setEditTagValue] = useState('');

  const addTask = () => {
    if (newTask.trim()) {
      setTasks([...tasks, { 
        id: Date.now(), 
        text: newTask.trim(), 
        completed: false,
        tag: newTag || null
      }]);
      setNewTask('');
      setNewTag('');
    }
  };

  const addCustomTag = (tagName) => {
    if (tagName.trim() && !getAllTags().includes(tagName.trim())) {
      setCustomTags([...customTags, tagName.trim()]);
    }
  };

  const editTag = (oldTag, newTag) => {
    if (newTag.trim() && oldTag !== newTag.trim()) {
      // Update tasks with the old tag
      setTasks(tasks.map(task => 
        task.tag === oldTag ? { ...task, tag: newTag.trim() } : task
      ));
      
      // Update custom tags array
      if (customTags.includes(oldTag)) {
        setCustomTags(customTags.map(tag => tag === oldTag ? newTag.trim() : tag));
      }
      
      // Update filter if it was set to the old tag
      if (filterTag === oldTag) {
        setFilterTag(newTag.trim());
      }
    }
    setEditingTag(null);
    setEditTagValue('');
  };

  const deleteTag = (tagToDelete) => {
    // Remove tag from all tasks
    setTasks(tasks.map(task => 
      task.tag === tagToDelete ? { ...task, tag: null } : task
    ));
    
    // Remove from custom tags
    setCustomTags(customTags.filter(tag => tag !== tagToDelete));
    
    // Clear filter if it was set to this tag
    if (filterTag === tagToDelete) {
      setFilterTag('');
    }
  };

  const startEditingTag = (tag) => {
    setEditingTag(tag);
    setEditTagValue(tag);
  };

  const toggleTask = (id) => {
    setTasks(tasks.map(task => 
      task.id === id ? { ...task, completed: !task.completed } : task
    ));
  };

  const deleteTask = (id) => {
    setTasks(tasks.filter(task => task.id !== id));
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      addTask();
    }
  };

  const getAllTags = () => {
    const taskTags = tasks.map(task => task.tag).filter(tag => tag);
    return [...new Set([...customTags, ...taskTags])];
  };

  const getFilteredTasks = () => {
    if (!filterTag) return tasks;
    return tasks.filter(task => task.tag === filterTag);
  };

  return (
    <div className="min-h-screen bg-gray-900 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <div className="bg-gray-800 rounded-2xl shadow-lg border border-gray-700 overflow-hidden">
          {/* Header */}
          <div className="p-6 border-b border-gray-700">
            <h1 className="text-xl font-bold text-gray-100 text-center">Clean Slate</h1>
          </div>
          
          {/* Add Task Input */}
          <div className="p-4 border-b border-gray-700 space-y-3">
            <div className="flex gap-2">
              <input
                type="text"
                value={newTask}
                onChange={(e) => setNewTask(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Add a new task..."
                className="flex-1 px-4 py-3 text-sm text-gray-200 bg-gray-700 border-0 rounded-xl focus:outline-none focus:ring-2 focus:ring-gray-600 focus:bg-gray-600 transition-all placeholder-gray-400"
              />
              <button
                onClick={addTask}
                className="w-12 h-12 bg-gray-100 hover:bg-white text-gray-800 rounded-xl flex items-center justify-center transition-colors focus:outline-none focus:ring-2 focus:ring-gray-500"
              >
                <Plus size={18} />
              </button>
            </div>
            
            {/* Tag Input */}
            <div className="flex gap-2 items-center">
              <Tag size={16} className="text-gray-400" />
              <select
                value={newTag}
                onChange={(e) => setNewTag(e.target.value)}
                className="flex-1 px-3 py-2 text-xs text-gray-300 bg-gray-700 border-0 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-600 focus:bg-gray-600 transition-all"
              >
                <option value="">No tag</option>
                {customTags.map(tag => (
                  <option key={tag} value={tag}>{tag}</option>
                ))}
              </select>
              <input
                type="text"
                placeholder="New tag..."
                className="w-20 px-2 py-2 text-xs text-gray-300 bg-gray-700 border-0 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-600 focus:bg-gray-600 transition-all placeholder-gray-500"
                onKeyPress={(e) => {
                  if (e.key === 'Enter' && e.target.value.trim()) {
                    addCustomTag(e.target.value);
                    setNewTag(e.target.value.trim());
                    e.target.value = '';
                  }
                }}
              />
            </div>
            
            {/* Tag Filter */}
            <div className="flex gap-1 flex-wrap">
              <button
                onClick={() => setFilterTag('')}
                className={`px-3 py-1 text-xs rounded-full transition-all ${
                  filterTag === '' 
                    ? 'bg-gray-100 text-gray-900' 
                    : 'bg-gray-600 text-gray-300 hover:bg-gray-500'
                }`}
              >
                All
              </button>
              {getAllTags().map(tag => (
                <div key={tag} className="flex items-center gap-1">
                  {editingTag === tag ? (
                    <div className="flex items-center gap-1">
                      <input
                        type="text"
                        value={editTagValue}
                        onChange={(e) => setEditTagValue(e.target.value)}
                        onKeyPress={(e) => {
                          if (e.key === 'Enter') {
                            editTag(tag, editTagValue);
                          } else if (e.key === 'Escape') {
                            setEditingTag(null);
                            setEditTagValue('');
                          }
                        }}
                        className="px-2 py-1 text-xs rounded-full bg-gray-600 border border-gray-500 focus:outline-none focus:ring-1 focus:ring-gray-400 min-w-0 w-16 text-gray-200"
                        autoFocus
                      />
                      <button
                        onClick={() => editTag(tag, editTagValue)}
                        className="w-4 h-4 text-green-400 hover:text-green-300 transition-colors"
                      >
                        <Save size={12} />
                      </button>
                    </div>
                  ) : (
                    <div className="flex items-center">
                      <button
                        onClick={() => setFilterTag(tag)}
                        className={`px-3 py-1 text-xs rounded-l-full transition-all ${
                          filterTag === tag 
                            ? 'bg-gray-100 text-gray-900' 
                            : 'bg-gray-600 text-gray-300 hover:bg-gray-500'
                        }`}
                      >
                        {tag}
                      </button>
                      {!customTags.includes(tag) && (
                        <div className="flex">
                          <button
                            onClick={() => startEditingTag(tag)}
                            className="w-5 h-5 bg-gray-600 hover:bg-gray-500 text-gray-400 hover:text-gray-300 transition-colors flex items-center justify-center"
                          >
                            <Edit3 size={10} />
                          </button>
                          <button
                            onClick={() => deleteTag(tag)}
                            className="w-5 h-5 bg-gray-600 hover:bg-red-600 text-gray-400 hover:text-red-300 transition-colors rounded-r-full flex items-center justify-center"
                          >
                            <X size={10} />
                          </button>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>

          {/* Task List */}
          <div className="max-h-96 overflow-y-auto">
            {getFilteredTasks().length === 0 ? (
              <div className="p-8 text-center text-gray-400 text-sm">
                {filterTag ? `No tasks with "${filterTag}" tag.` : 'No tasks yet. Add one above.'}
              </div>
            ) : (
              <div className="divide-y divide-gray-700">
                {getFilteredTasks().map((task) => (
                  <div
                    key={task.id}
                    className="flex items-center gap-3 p-4 hover:bg-gray-700 transition-colors group"
                  >
                    <button
                      onClick={() => toggleTask(task.id)}
                      className={`w-5 h-5 rounded-full border-2 flex items-center justify-center transition-all ${
                        task.completed
                          ? 'bg-gray-100 border-gray-100 text-gray-800'
                          : 'border-gray-500 hover:border-gray-400'
                      }`}
                    >
                      {task.completed && <Check size={12} />}
                    </button>
                    
                    <div className="flex-1 flex flex-col gap-1">
                      <span
                        className={`text-sm transition-all ${
                          task.completed
                            ? 'text-gray-500 line-through'
                            : 'text-gray-200'
                        }`}
                      >
                        {task.text}
                      </span>
                      {task.tag && (
                        <span className="text-xs text-gray-400 bg-gray-700 px-2 py-0.5 rounded-full w-fit border border-gray-600">
                          {task.tag}
                        </span>
                      )}
                    </div>
                    
                    <button
                      onClick={() => deleteTask(task.id)}
                      className="w-6 h-6 text-gray-500 hover:text-red-400 transition-colors opacity-0 group-hover:opacity-100"
                    >
                      <X size={14} />
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Footer Stats */}
          {tasks.length > 0 && (
            <div className="p-4 border-t border-gray-700 bg-gray-750">
              <div className="text-xs text-gray-400 text-center">
                {getFilteredTasks().filter(task => !task.completed).length} of {getFilteredTasks().length} remaining
                {filterTag && ` in "${filterTag}"`}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}